import React from "react";

import ToggleButton from "../components/ToggleButton/ToggleButton";

import "../styles/home/homeStyle.scss";

function Home(){
    return (
        <>
            <div className="container-fluid text-center">
                <h1 className="header-main-home">Boba</h1>
                <hr />
            </div>

            <div className="container text-center">
                <div className="row">
                    <div className="btn-toggle-style col col-sm col-md">
                        <ToggleButton title="php server" />
                    </div>
                    <div className="btn-toggle-style col col-sm col-md">
                        <ToggleButton title="dns server" />
                    </div>
                    <div className="btn-toggle-style col col-sm col-md">
                        <ToggleButton title="db server" />
                    </div>
                    <div className="btn-toggle-style col col-sm col-md">
                        <ToggleButton title="config" />
                    </div>
                </div>
            </div>
        </>
    );
}

export default Home;