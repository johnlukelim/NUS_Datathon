import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import SurveyAnalyticsDashboard from './SurveyAnalyticsDashboard.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <SurveyAnalyticsDashboard />
  </StrictMode>
);
