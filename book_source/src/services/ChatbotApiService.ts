// frontend/src/services/ChatbotApiService.ts
import { UserQuery, ChatbotResponse } from '@site/src/types';

const API_BASE_URL = 'http://localhost:8000'; // Make sure this matches your backend URL

export const ChatbotApiService = {
  fetchChatResponse: async (query: UserQuery): Promise<ChatbotResponse> => {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(query),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to fetch chatbot response');
    }

    return response.json();
  },
};
