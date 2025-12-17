// frontend/src/types.ts (Placeholder for shared types)
import { Chunk } from '../../backend/src/models/data_models'; // Adjust path if needed

export interface UserQuery {
  query: string;
  context_type: 'full_book' | 'selected_text';
  selected_text?: string;
}

export interface ChatbotResponse {
  answer: string;
  source_chunks: Chunk[];
  response_time_ms: number;
}
