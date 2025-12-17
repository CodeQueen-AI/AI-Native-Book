import React from 'react';
import './FloatingChatbotButton.css';

interface FloatingChatbotButtonProps {
  onClick: () => void;
  isOpen: boolean;
}

const FloatingChatbotButton: React.FC<FloatingChatbotButtonProps> = ({ onClick, isOpen }) => {
  return (
    <button
      className={`floating-chatbot-button ${isOpen ? 'open' : ''}`}
      onClick={onClick}
      aria-label={isOpen ? 'Close Chatbot' : 'Open Chatbot'}
    >
      🤖
    </button>
  );
};

export default FloatingChatbotButton;