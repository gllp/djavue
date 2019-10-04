import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    get_user_details(username) {
        return get('/api/get_user_details', {username: username});
    },
    follow(username){
        return post('/api/follow', {username: username});
    },
    unfollow(username){
        return post('/api/unfollow', {username: username});
    },
    list_questions(username){
        return get('/api/list_questions', {username: username});
    },
    get_question(question_title, author_username){
        return get('/api/get_question', {question_title: question_title, author_username: author_username});
    },
    get_answers(question_title, author_username){
        return get('/api/get_answers', {question_title: question_title, author_username: author_username});
    },
    post_question(text) {
        return post('/api/post_question', {text: text})
    },
    post_answer(question_title, author_username, text) {
        return post('/api/post_answer', {question_title: question_title, author_username: author_username, text: text})
    },
    users_list(username){
        return get('/api/users_list', {username: username});
    },
    post_new_user(user){
        return post('/api/post_new_user', {user: JSON.stringify(user)})
    },
    get_profile(username){
        return get('/api/get_profile', {username: username})
    },
}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}
