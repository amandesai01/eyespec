function PDFAsset() {
  return (
    <div
      tabIndex={0}
      className="collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-4 w-1/2 mx-auto"
    >
      <div className="collapse-title text-xl font-medium flex items-center">
        <img src="file-1453.svg" alt="file" className="w-8 h-8 mr-2" />
        JHU APL Building 14 Systems Integration 3
      </div>
      <div className="collapse-content">
        <div className="flex justify-center">
          <button className="btn btn-sm gap-2 mr-4">
            <img src="download-4177.svg" alt="file" className="w-4 h-4 mr-2" />
            Download PDF
          </button>
          <button className="btn btn-sm btn-outline gap-2">
            <img src="excel-4955.svg" alt="file" className="w-4 h-4 mr-2" />
            Download Excel
          </button>
        </div>
      </div>
    </div>
  );
}

export default PDFAsset;
