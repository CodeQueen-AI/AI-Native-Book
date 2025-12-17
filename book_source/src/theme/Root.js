import React from 'react';
import { ChatbotUIProvider } from '@site/src/context/ChatbotUIContext';
import FloatingChatbotButton from '@site/src/components/FloatingChatbotButton';
import ChatbotPanel from '@site/src/components/ChatbotPanel';
import { useChatbotUI } from '@site/src/context/ChatbotUIContext';


// Default implementation, that you can customize
function Root({ children }) {
  const { isChatbotOpen, toggleChatbot } = useChatbotUI();
  return (
    <>
      {children}
      <FloatingChatbotButton onClick={toggleChatbot} isOpen={isChatbotOpen} />
      <ChatbotPanel isOpen={isChatbotOpen} onClose={toggleChatbot} />
    </>
  );
}

export default function RootWrapper(props) {
  return (
    <ChatbotUIProvider>
      <Root {...props} />
    </ChatbotUIProvider>
  );
}
