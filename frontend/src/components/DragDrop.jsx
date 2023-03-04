import React, { useState } from "react";
import { FileUploader } from "react-drag-drop-files";

const fileTypes = ["pdf"];

function DragDrop({ processFile }) {
  const [file, setFile] = useState();

  const addFile = (file) => {
    console.log("File Attached  ");
    setFile(file);
  };

  const uploadFile = () => {
    console.log("Uploading file");
    processFile((prevState) => [...prevState, file]);
  };
  return (
    <>
      <FileUploader handleChange={addFile} name="file" types={fileTypes} />
      {file ? (
        <button className={`btn btn-outline ml-5`} onClick={uploadFile}>
          Upload
        </button>
      ) : null}
    </>
  );
}

export default DragDrop;
