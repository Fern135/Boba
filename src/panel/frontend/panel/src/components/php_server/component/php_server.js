import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/php_server.scss';

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
        fetchProjects();
    }, []);

    const handleProjectChange = (event) => {
        const selectedValue = event.target.value;
        setSelectedProject(selectedValue);
        fetchProjectDetails(selectedValue);
    };

    const PhpLogs = () => {
        return (
            <div className='border PhpLogs'>
                <p className='green'>
                    {isRunning}
                    {/* {console.log(isRunning)} */}
                </p>
            </div>
        );
    };

    return (
        <div className="container border">
            <h1>Php Server</h1>
            <hr />

            <div className='row'>
                <div className="col col-sm col-md">
                    <button
                        className={`btn btn-block ${isRunning ? 'btn-success' : 'btn-danger'}`}
                        onClick={toggleRunning}
                    >
                        <h3>{isRunning ? 'Start Server' : 'Stop Server'}</h3>
                    </button>

                    <hr />

                    <div className="status-container">
                        <div className={`circle ${isRunning ? 'red' : 'green'}`} />
                        <h3>Status</h3>
                    </div>
                </div>

                <div className="col col-sm col-md">
                    <PhpLogs />
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
