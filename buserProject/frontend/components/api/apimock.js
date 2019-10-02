import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },
    list_tweets(){
        return mockasync(
            [{
                author_name: 'Albert Einstein',
                author_username: '@alberteinstein',
                author_avatar: 'https://escolaeducacao.com.br/wp-content/uploads/2018/11/albert-einstein-biografia-750x430.jpg',
                created_at: '43 min',
                text: 'A bomba atômica é uma das sequelas mais horrendas da humanidade'
            },
            { divider: true, inset: false },
            {
                author_name: 'Michael Jackson',
                author_username: '@mjackson',
                author_avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQQvKGLPvPTHVPZ0baxBJb_EcoOYD72PTGdHsnAgpjWadUxiH2A',
                created_at: '1 h',
                text: 'Why? Why? Tell them that\'s human nature' 
            },
            { divider: true, inset: false },
            {
                author_name: 'George Micael',
                author_username: '@gmichael',
                author_avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSFNubinejiQCzktzhOyaoLc_BpB7CqoErwsMyzNAWxFOa7srz2',
                created_at: '2 h',
                text: 'Careless Whisper everywhere!!' 
        }]);
    }
};

export default api;
