import React from 'react';
import DocItemContent from '@theme-original/DocItem/Content';
import ChatbotWidget from '@site/src/components/ChatbotWidget';
import { ChatbotApiService } from '@site/src/services/ChatbotApiService';

export default function DocItemContentWrapper(props) {
  return (
    <div style={{ display: 'flex', flexDirection: 'row' }}>
      <div style={{ flex: 1 }}>
        <DocItemContent {...props} />
      </div>
      <div style={{ flex: '0 0 400px', marginLeft: '20px' }}>
        <ChatbotWidget chatbotService={ChatbotApiService} />
      </div>
    </div>
  );
}
