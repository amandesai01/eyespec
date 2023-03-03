import Navbar from "./Navbar";
import DragDrop from "./DragDrop";
import PDFAsset from "./PDFAsset";

function Home() {
  return (
    <>
      <Navbar />
      <div className="p-10 mx-auto">
        <div className="flex justify-center items-center py-4">
          <DragDrop />
        </div>
        <hr />
        <PDFAsset />
      </div>
    </>
  );
}

export default Home;
