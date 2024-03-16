
// mod libs;

// use libs::Search;

/*
    todo:
        make Threads "class": []
            - add method to search for a string in
            
        make DNS server:
            [] - run on a thread
            [] - use more threads for dns server if needed
            [] - run locally only
            [] - read conf.json and use conf['domains'][0]["domain"]  to get the domain name where 0 is each 
                index in domains[] array and "domain" is the domain name 
                and conf['domains'][0]["route"] is the project route
            
        make php server:
            [] - run on a thread
            [] - use more threads for php server if needed
            [] - make entry point scalable (means the entry point per project can and will change)

        make mysql server:
            [] - run on a thread
            [] - use more threads for mysql server if needed

        #region thread will run as soon as program starts
            make panel front-end (react): 
                [] - run on a thread
                [] - button for toggling php server (on / off)
                [] - button for toggling DNS server (on / off)
                [] - button for toggling mysql server (on / off)

            make panel backend (django): 
                [] - run on a thread
                [] - activate / deactivate php, dns, and mysql server. make rust api connect with django? 
                [] - database will save per user config. dns domains will be saved in conf.json unless it reaches a certain limit
                    then i'll save it on the .db django database
        #endregion
*/

fn main() {
    println!("Hello, world!");
}
