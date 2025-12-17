export interface ChunkMetadata {
  file_path: string;
  page: number | string;
}

export interface Chunk {
  text: string;
  metadata: ChunkMetadata;
}

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
