import React, { createContext, useContext, useState, ReactNode } from 'react';

interface ChatbotUIContextType {
  isChatbotOpen: boolean;
  toggleChatbot: () => void;
}

const ChatbotUIContext = createContext<ChatbotUIContextType | undefined>(undefined);

export const ChatbotUIProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  const toggleChatbot = () => {
    setIsChatbotOpen((prev) => !prev);
  };

  return (
    <ChatbotUIContext.Provider value={{ isChatbotOpen, toggleChatbot }}>
      {children}
    </ChatbotUIContext.Provider>
  );
};

export const useChatbotUI = () => {
  const context = useContext(ChatbotUIContext);
  if (context === undefined) {
    throw new Error('useChatbotUI must be used within a ChatbotUIProvider');
  }
  return context;
};
