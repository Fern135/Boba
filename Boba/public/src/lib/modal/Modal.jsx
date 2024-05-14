import React, { useState, useEffect } from "react";

import "../../../Global.scss";

function Modal({ title, body, isVisible }) {
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    setShowModal(isVisible);
  }, [isVisible]);

  const handleClose = () => setShowModal(false);
  const handleShow = () => setShowModal(true);

  return (
    <>
      <button className="btn btn-primary" onClick={handleShow}>
        Open Modal
      </button>

      <div className={`modal fade${showModal ? " show" : ""}`} tabIndex="-1" style={{ display: showModal ? "block" : "none" }}>
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">
                {title}
              </h5>
              <button type="button" className="btn-close" aria-label="Close" onClick={handleClose}></button>
            </div>
            <div className="modal-body">
                {body}
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" onClick={handleClose}>Close</button>
              <button type="button" className="btn btn-primary" onClick={handleClose}>Save Changes</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Modal;


/*
example usage
    import React, { useState } from "react";
import Modal from "./Modal";

function App() {
  const [isModalVisible, setIsModalVisible] = useState(false);

  const handleOpenModal = () => {
    setIsModalVisible(true);
  };

  const handleCloseModal = () => {
    setIsModalVisible(false);
  };

  return (
    <div>
      <button className="btn btn-primary" onClick={handleOpenModal}>
        Open Modal
      </button>
      
      <Modal
        title="Modal Title"
        body="This is the content of the modal. You can put any content here."
        isVisible={isModalVisible}
      />
    </div>
  );
}

export default App;

*/