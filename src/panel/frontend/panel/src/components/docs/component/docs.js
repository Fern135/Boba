import React, {
    useEffect,
    useState
} from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';

import "../style/docs.scss";

function Docs(){

    return (
        <div className="container">
            <a href="/" className="btn btn-outline-success deco-a-none">
                Home
            </a>

            <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#demo">
                Open Offcanvas Sidebar
            </button>

            <div>
                <h1 className="title">Documentation</h1>
            </div>
        </div>
    );
}

export default Docs;