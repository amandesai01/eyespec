import Navbar from "./Navbar";
import DragDrop from "./DragDrop";
import PDFAsset from "./PDFAsset";
import { useEffect, useState } from "react";
import NewPDFAsset from "./NewPDFAsset";

function Home() {
  const [currentFiles, setCurrentFiles] = useState([]);
  const [newFiles, setNewFiles] = useState([]);

  useEffect(() => {
    const loadFiles = async () => {
      // loading file login goes here
      setCurrentFiles([{ name: "JHU APL Building 14 Systems Integration 3" }]);
    };
    loadFiles();
  }, []);

  useEffect(() => {
    console.log(newFiles);
  }, [newFiles]);

  return (
    <>
      <Navbar />
      <div className="p-10 mx-auto">
        <div className="flex justify-center items-center py-4">
          <DragDrop processFile={setNewFiles} />
        </div>
        <hr />
        {newFiles.length
          ? newFiles.map((file) => <NewPDFAsset name={file.name} key={file} />)
          : null}
        {currentFiles.length
          ? currentFiles.map((file) => <PDFAsset name={file.name} key={file} />)
          : null}
      </div>
    </>
  );
}

export default Home;
