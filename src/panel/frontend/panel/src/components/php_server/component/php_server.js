import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


import '../style/php_server.scss';

import browser from "../../../lib/browser/browser";

function PhpServer() {
    const [isRunning,              setIsRunning] = useState(true);
    const [projects,                setProjects] = useState([]);
    const [selectedProject,  setSelectedProject] = useState('');
    const [projectDetails,    setProjectDetails] = useState({});

    const toggleRunning = () => {
        setIsRunning(!isRunning);
    };

    const fetchProjects = async () => {
        try {
            const response = await axios.get('/api/projects'); // Replace with your server API endpoint
            setProjects(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const fetchProjectDetails = async (projectId) => {
        try {
            const response = await axios.get(`/api/projects/${projectId}`); // Replace with your server API endpoint
            setProjectDetails(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        // fetchProjects();

        console.log(browser.getFullDebugInfo());
    }, []);

    const handleProjectChange = (event) => {
        const selectedValue = event.target.value;
        setSelectedProject(selectedValue);
        fetchProjectDetails(selectedValue);
    };

    return (
        <div className="container border">
            <h1>Php Server</h1>
            <hr />

            <div className='row'>
                
                <div className="col col-sm col-md">
                    <div className="status-container">
                        <button
                            className={`btn btn-block ${isRunning ? 'btn-success' : 'btn-danger'}`}
                            onClick={toggleRunning}
                        >
                            <h3>{isRunning ? 'Start Server' : 'Stop Server'}</h3>
                        </button>
                        
                        <div className="container">
                            <h3 id="status">Status</h3>
                            <div id="circle" className={`circle ${isRunning ? 'red' : 'green'}`} />
                        </div>

                    </div>
                </div>

                <div className='row'>
                    <div className="col col-sm col-md border">
                        <h3>Project:</h3>
                        <select id='project-select-main' value={selectedProject} onChange={handleProjectChange}>
                            <option value="">Select a project</option>

                            {projects.map((project, index) => (
                                <option key={index} value={project.id}>
                                    {project.name}
                                </option>
                            ))}

                        </select>

                        {selectedProject && (
                            <div>
                                <h4>
                                    Domain name: {projectDetails.domainName}
                                    <br />
                                    Project path: {projectDetails.projectPath}
                                    <br />
                                    PHP version: {projectDetails.phpVersion}
                                </h4>
                            </div>
                        )}

                    </div>
                </div>
            </div>
        </div>
    );
}

export default PhpServer;


/*
    real life demo for including students to the university page.

    check apis
    check controllers
    check json returns and how it's being rendered.

    interlocutor?

    my duties with this client: Luis Diez.

        1.  Fernando con camila
        2.  via me on what's app

        TODO:
            note taking for meetings, 

            git set up 
            git clone 

            set up php enviroment

    next week thursday at 10 am 
    
    then every tuesday? maybe? 

    view if ssh key is generated mac / linux:
        ls -al ~/.ssh

    view public key: mac / linux
        cat ~/.ssh/id_rsa.pub

    ssh key for git lab:
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWQzG42BvNS60vizx64IL0+ClknRtmIP5jyCleIBjT/+zd1ALZU3uO16ko5iSlUIdpFpZqE9dHdrVuT4GKpgBjD0LWxP0EIBp5RMAMZakPY4gdwvXzrvy4SHaxzgQ1kFz7lbkNznmlzEVItuHq4b7OPyl7TKN+W3dTV5mrzgzMpKQp7hNhLdmpdI2vrtCNWNkOp+s4Qt3RRaFYQOngMQpHS8S/CwTNurVW23qJuFAfNI9v/qLv71ExYEKzLq9xBW20/VDXFQQYAt8SG27mYjNX2+D0bLD0lJq9IxbBhmLPWLl1SIFklAhd6TEZ4Egm+srdLPGNs9cbENy7/9OzKymxxkTs5kTOm9cUQBur11XAJuPMIS8ZyGwozdlvLhA4XIZQhrpm8HBoidMdSdCOCX+cxOkAN1qv9RxGimGod/3owGbqxBVBVTbKdCCpKM+/8L/zFRw11qLxeFvlVLlEcwsazG9Fac7Fk+63k30FghOHf+W0NNnp2JUP1j9gJbOfhgU= patriotkeyl.l.c@Fernandos-MBP

    also set up for windows. just in case i'm working from my windows pc
*/