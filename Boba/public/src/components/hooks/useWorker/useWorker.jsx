import { useState, useEffect } from 'react';

function useWorker(workerScript) {
    const [worker, setWorker] = useState(null);
    const [result, setResult] = useState(null);

    useEffect(() => {
        const newWorker = new Worker(workerScript);

        // Handle messages from the worker
        newWorker.onmessage = function(event) {
            setResult(event.data);
        };

        // Return the worker instance
        setWorker(newWorker);

        // Clean up the worker when the component unmounts
        return () => {
            newWorker.terminate();
        };
    }, [workerScript]);

    // Function to send data to the worker
    const postMessage = (data) => {
        if (worker) {
            worker.postMessage(data);
        }
    };

    // Function to handle async tasks in the worker
    const runAsyncTask = async (task) => {
        return new Promise((resolve, reject) => {
            const messageHandler = (event) => {
                worker.removeEventListener('message', messageHandler);
                resolve(event.data);
            };
            worker.addEventListener('message', messageHandler);
            worker.postMessage(task);
        });
    };

    return { result, postMessage, runAsyncTask };
}

export default useWorker;



// usage
/*
    import React, { useState } from 'react';
    import useWorker from './useWorker';

    function MyComponent() {
        const [inputData, setInputData] = useState('');
        const { result, postMessage, runAsyncTask } = useWorker('./worker.js');

        const handleStartWorker = async () => {
            Example of running an asynchronous task in the worker
            const asyncResult = await runAsyncTask(inputData);
            console.log('Async result:', asyncResult);
        };

        return (
            <div>
                <input
                    type="text"
                    value={inputData}
                    onChange={(e) => setInputData(e.target.value)}
                />
                <button onClick={handleStartWorker}>Start Worker</button>
                {result && <p>Result: {result}</p>}
            </div>
        );
    }

    export default MyComponent;
*/