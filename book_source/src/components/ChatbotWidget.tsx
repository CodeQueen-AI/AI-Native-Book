// frontend/src/components/ChatbotWidget.tsx
import React, { useState } from 'react';
import './ChatbotWidget.css'; // Assuming some CSS for styling
// import useChatbot from '../hooks/useChatbot';
import useChatbot from '@site/src/hooks/useChatbot';
import { UserQuery, ChatbotResponse } from '@site/src/types';

interface ChatbotService {
  fetchChatResponse: (query: UserQuery) => Promise<ChatbotResponse>;
}

interface ChatbotWidgetProps {
  chatbotService: ChatbotService;
}

export const ChatbotWidget: React.FC<ChatbotWidgetProps> = ({ chatbotService }) => {
  const [query, setQuery] = useState('');
  const [selectedText, setSelectedText] = useState('');
  const { response, isLoading, error, sendFullBookQuery, sendSelectedTextQuery } = useChatbot(chatbotService);

  const handleQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    if (selectedText.trim()) {
      await sendSelectedTextQuery(query, selectedText);
    } else {
      await sendFullBookQuery(query);
    }
    setQuery('');
    setSelectedText('');
  };

  return (
    <div className="chatbot-widget-container">
      <h3>Docusaurus Chatbot</h3>
      <form onSubmit={handleQuery}>
        <textarea
          placeholder="Selected text context (optional)"
          value={selectedText}
          onChange={(e) => setSelectedText(e.target.value)}
          rows={3}
          className="selected-text-input"
        ></textarea>
        <input
          type="text"
          placeholder="Ask a question about the book..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="query-input"
        />
        <button type="submit" disabled={isLoading} className="send-button">
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>

      {response && (
        <div className="chatbot-response">
          <h4>Answer:</h4>
          <p>{response.answer}</p>
          <h5>Sources:</h5>
          <ul>
            {Array.isArray(response.source_chunks) && response.source_chunks.map((chunk: any, index: number) => (
              <li key={index}>"{chunk.text.substring(0, Math.min(chunk.text.length, 200))}" (from {chunk.metadata.file_path})</li>
            ))}
          </ul>
          <p className="response-time">Response time: {response.response_time_ms ? response.response_time_ms.toFixed(2) : 'N/A'}ms</p>
        </div>
      )}
    </div>
  );
};

export default ChatbotWidget;