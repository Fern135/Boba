import React, { 
    // useEffect,
    useState 
} from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/php_server.scss';

function PhpServer() {
    const [isRunning, setIsRunning] = useState(true);

    const toggleRunning = () => {
        setIsRunning(!isRunning);
    };

    const PhpLogs = () => {
        return(
            <div className='border PhpLogs'>
                <p className='green'>
                    {isRunning}
                    {/* {console.log(isRunning)} */}
                </p>
            </div>
        );
    };

    // useEffect(() => {
    //     PhpLogs();
    // });

    return (
        <div className="container border">
            <h1>
                Php Server
            </h1>
            <hr></hr>

            <div className='row'>
                <div className="col col-sm col-md">
                    <button
                        className={`btn btn-block ${isRunning ? 'btn-success' : 'btn-danger'}`}
                        onClick={toggleRunning}
                    >
                    <h3>{isRunning ? 'Start Server' : 'Stop Server'}</h3>
                    </button>

                    <hr></hr>
                    
                    <div className="status-container">
                        <div className={`circle ${isRunning ? 'red' : 'green'}`} />
                        <h3>Status</h3>
                    </div>
                </div>

                <div className="col col-sm col-md">
                    <PhpLogs />
                </div>

            </div>
        </div>
    );
}

export default PhpServer;
