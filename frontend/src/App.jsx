import { useState } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import DragDrop from './components/DragDrop';
import PDFAsset from './components/PDFAsset';

function App() {
  return (
    <>
    <Navbar/>
    <div className="p-10 mx-auto">
      <div className="flex justify-center items-center py-4">
        <DragDrop/>
      </div>
      <hr/>
      <PDFAsset/>
    </div>
    </>
  );
}

export default App;
