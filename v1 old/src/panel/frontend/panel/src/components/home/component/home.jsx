import React, {
    useEffect,
    useState
} from 'react';

// import 'bootstrap/dist/css/bootstrap.min.css';

/********** used components **********/
import PhpServer from "../../php_server/component/php_server"
/********** used components **********/

/********** styling **********/
import "../style/home.scss"
/********** styling **********/


function Home(){
    const [isSticky, setIsSticky] = useState(false);

    useEffect(() => {
      const handleScroll = () => {
        if (window.scrollY > 0) {
          setIsSticky(true);
        } else {
          setIsSticky(false);
        }
      };
  
      window.addEventListener('scroll', handleScroll);
  
      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    }, []);

  
    return (
      <div>
        <header className={`sticky-header ${isSticky ? 'sticky' : ''}`}>
          <nav>
            {/* Your navigation content goes here */}
              <h1>
                Boba
              </h1>


          </nav>
        </header>

        <div className="container">
          <div className="row">
            <div className="col col-sm col-md">
              <PhpServer />
            </div>

            {/* <div className="col col-sm col-md">
            </div> */}

          </div>
        </div>

      </div>
    );
}

export default Home;