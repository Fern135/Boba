export default class WebWorkerHandler {
    constructor(workerScriptPath) {
        this.worker = new Worker(workerScriptPath);
        this.messageHandlers = {};

        // Listen for messages from the worker
        this.worker.onmessage = (event) => {
            const { type, data } = event.data;
            const handler = this.messageHandlers[type];
            if (handler) {
                handler(data);
            }
        };
    }

    // Send a message to the worker
    postMessage(type, data) {
        this.worker.postMessage({ type, data });
    }

    // Register a message handler for a specific message type
    onMessage(type, handler) {
        this.messageHandlers[type] = handler;
    }

    // Terminate the worker
    terminate() {
        this.worker.terminate();
    }
}
/*
    example usage
    useEffect(() => {
        Create a new web worker handler
        const workerHandler = new WebWorkerHandler('/path-to-your-worker-script.js');

        Send a message to the worker
        workerHandler.postMessage('calculate', { x: 10, y: 5 });

        Register a message handler for the 'result' message type
        workerHandler.onMessage('result', (data) => {
            console.log('Received result from worker:', data);
        });

        return () => {
            Terminate the worker when the component unmounts
            workerHandler.terminate();
        };
    }, []);

*/