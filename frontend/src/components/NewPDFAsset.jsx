import { useEffect, useState } from "react";

function NewPDFAsset({ name, pdfAssetLink, excelAssetLink }) {
  const [isProcessing, setIsProcessing] = useState(true);
  const [excelBtnText, setExcelBtnText] = useState("Processing Excel");

  // using useEffect only for UI testing
  // Replace it with listener function to processing task
  useEffect(() => {
    setTimeout(() => {
      setIsProcessing(false);
      setExcelBtnText("Download Excel");
    }, 7000);
  }, []);
  return (
    <div
      tabIndex={0}
      className="collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-4 w-1/2 mx-auto"
    >
      <div className="collapse-title text-xl font-medium flex items-center">
        <img src="file-1453.svg" alt="file" className="w-8 h-8 mr-2" />
        {name}
      </div>
      <div className="collapse-content">
        <div className="flex justify-center">
          <button className="btn btn-sm gap-2 mr-4">
            <img src="download-4177.svg" alt="file" className="w-4 h-4 mr-2" />
            Download PDF
          </button>
          <button
            className={`btn btn-sm btn-outline gap-2 ${
              isProcessing ? "loading" : ""
            }`}
          >
            {isProcessing ? null : (
              <img src="excel-4955.svg" alt="file" className="w-4 h-4 mr-2" />
            )}
            {excelBtnText}
          </button>
        </div>
      </div>
    </div>
  );
}

export default NewPDFAsset;
