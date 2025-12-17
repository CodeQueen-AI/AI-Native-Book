import React from 'react';
import './ChatbotPanel.css';
import ChatbotWidget from '@site/src/components/ChatbotWidget';
import { ChatbotApiService } from '@site/src/services/ChatbotApiService';

interface ChatbotPanelProps {
  isOpen: boolean;
  onClose: () => void;
}

const ChatbotPanel: React.FC<ChatbotPanelProps> = ({ isOpen, onClose }) => {
  return (
    <div className={`chatbot-panel ${isOpen ? 'open' : ''}`}>
      <div className="chatbot-panel-header">
        <button className="chatbot-panel-close-button" onClick={onClose}>
          &times;
        </button>
      </div>
      <div className="chatbot-panel-content">
        <ChatbotWidget chatbotService={ChatbotApiService} />
      </div>
    </div>
  );
};

export default ChatbotPanel;