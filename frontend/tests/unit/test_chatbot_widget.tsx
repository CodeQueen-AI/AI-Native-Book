// frontend/tests/unit/test_chatbot_widget.tsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import ChatbotWidget from '../../src/components/ChatbotWidget'; // Adjust path as needed

// Mock the backend API calls
jest.mock('../../src/services/api', () => ({ // Assuming an API service exists
  fetchChatResponse: jest.fn(() =>
    Promise.resolve({
      answer: 'Mocked answer for full book query.',
      source_chunks: [{ text: 'Source 1', metadata: { file_path: 'doc1.md' } }],
    })
  ),
  fetchSelectedTextChatResponse: jest.fn(() =>
    Promise.resolve({
      answer: 'Mocked answer for selected text query.',
      source_chunks: [{ text: 'Selected source 1', metadata: { file_path: 'doc2.md' } }],
    })
  ),
}));

describe('ChatbotWidget', () => {
  test('T039: renders and handles full-book query', async () => {
    render(<ChatbotWidget />);
    const input = screen.getByPlaceholderText(/Ask a question/i);
    const sendButton = screen.getByRole('button', { name: /send/i });

    userEvent.type(input, 'What is Physical AI?');
    userEvent.click(sendButton);

    expect(await screen.findByText('Mocked answer for full book query.')).toBeInTheDocument();
    expect(screen.getByText('Source 1')).toBeInTheDocument();
  });

  test('T040: handles selected text query input', async () => {
    render(<ChatbotWidget />);
    const input = screen.getByPlaceholderText(/Ask a question/i);
    const selectedTextInput = screen.getByPlaceholderText(/Selected text context/i);
    const sendButton = screen.getByRole('button', { name: /send/i });

    userEvent.type(input, 'Explain this text.');
    userEvent.type(selectedTextInput, 'This is the selected text from the Docusaurus page.');
    userEvent.click(sendButton);

    expect(await screen.findByText('Mocked answer for selected text query.')).toBeInTheDocument();
    expect(screen.getByText('Selected source 1')).toBeInTheDocument();
  });
});