import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


import '../style/php_server.scss';

import browser from "../../../lib/browser/browser";

function PhpServer() {
    // const [phpVersion,            setPhpVersion] = useState("");
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

    useEffect(() => { // as soon as the page loads
        // fetchProjects();

        console.log(browser.getFullDebugInfo()); // ! debugging
    }, []);

    const handleProjectChange = (event) => {
        const selectedValue = event.target.value;
        setSelectedProject(selectedValue);
        fetchProjectDetails(selectedValue);
    };

    return (
        <div className="container card bg-secondary">
            <div className="mx-auto php-server-card-title card-header">
                <h1>
                    PHP server
                </h1>
            </div>
            
            <hr />

            <div className='row card-body'>
                
                {/* php server */}
                <div className="col col-sm col-md">
                    <div className="status-container">
                        <button
                            id="start-stop-php-server"
                            className={`btn btn-block ${isRunning ? 'btn-success' : 'btn-danger'}`}
                            onClick={toggleRunning}
                        >
                            <h3>{isRunning ? 'Start' : 'Stop'}</h3>
                        </button>
                        
                        <div className="container d-flex flex-row-reverse">
                            <div id="Circle" className={`circle ${isRunning ? 'red' : 'green'}`} />
                            <h3 id="status" className='p-2'>Status</h3>
                        </div>

                    </div>
                </div>
                {/* php server */}

                {/* projects */}
                <div className='row'>
                    <div className="col col-sm col-md border projects-container-php">
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
                            <div className='container border'>
                                <h4>
                                    <input 
                                        type="hidden" 
                                        name="projectDetails.id" 
                                        value={projectDetails.id} 
                                    />
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
                {/* projects */}

            </div>
        </div>
    );
}

export default PhpServer;


