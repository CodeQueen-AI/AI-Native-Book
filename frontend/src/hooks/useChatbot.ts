// frontend/src/hooks/useChatbot.ts
import { useState, useCallback } from 'react';
import { UserQuery, ChatbotResponse } from '../types'; // Assuming types are defined

interface ChatbotService {
  fetchChatResponse: (query: UserQuery) => Promise<ChatbotResponse>;
}

const useChatbot = (chatbotService: ChatbotService) => {
  const [response, setResponse] = useState<ChatbotResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const sendQuery = useCallback(async (query: UserQuery) => {
    setIsLoading(true);
    setError(null);
    try {
      const res = await chatbotService.fetchChatResponse(query);
      setResponse(res);
    } catch (err) {
      setError('Failed to fetch chatbot response.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }, [chatbotService]);

  const sendFullBookQuery = useCallback(async (queryText: string) => {
    const query: UserQuery = { query: queryText, context_type: 'full_book' };
    await sendQuery(query);
  }, [sendQuery]);

  const sendSelectedTextQuery = useCallback(async (queryText: string, selectedText: string) => {
    const query: UserQuery = { query: queryText, context_type: 'selected_text', selected_text: selectedText };
    await sendQuery(query);
  }, [sendQuery]);

  return {
    response,
    isLoading,
    error,
    sendFullBookQuery,
    sendSelectedTextQuery,
  };
};

export default useChatbot;
