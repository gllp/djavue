import Vue from 'vue'

var logged_user = null;

const users_questions = {
        'alberteinstein': {
            author_name: 'Albert Einstein',
            author_username: 'alberteinstein',
            created_at: '2019-10-02T15:52:48.943372',
            title: 'What is E=mc²?',
        },
        'mjackson': {
            author_name: 'Michael Jackson',
            author_username: 'mjackson',
            created_at: '2019-10-02T15:52:22.771971',
            title: 'Why? Why? Tell them that\'s human nature. Is it true?',
        },
        'gmichael': {
            author_name: 'George Michael',
            author_username: 'gmichael',
            created_at: '2019-10-03T15:51:10.186087',
            title: 'Where are all the good songs nowadays?',
        }
    };

const users_details = {
    'alberteinstein': {
        username: 'alberteinstein',
        avatar : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROUX4e_XOhgUT9wGMnGM27F6S7f-oBr7OgxeUCXV3DXTKAKIfc',
        description: 'Doctor at John Hopkins Hospital',
        ifollow: false,
    },
    'mjackson': {
        username: 'mjackson',
        avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQQvKGLPvPTHVPZ0baxBJb_EcoOYD72PTGdHsnAgpjWadUxiH2A',
        description: 'Dentist at general Dental HealthCare Hospital',
        ifollow: false,
    },
    'gmichael': {
        username: 'gmichael',
        avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSFNubinejiQCzktzhOyaoLc_BpB7CqoErwsMyzNAWxFOa7srz2', 
        description : 'Phd in Physics by MIT',
        ifollow: false,
    }
}; 

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
    users_list(){
        return mockasync(
            [{
                username: 'alberteinstein',
                avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROUX4e_XOhgUT9wGMnGM27F6S7f-oBr7OgxeUCXV3DXTKAKIfc',
                description: 'Doctor at John Hopkins Hospital',
                ifollow: false,
            },
            {
                username: 'mjackson',
                avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQQvKGLPvPTHVPZ0baxBJb_EcoOYD72PTGdHsnAgpjWadUxiH2A',
                description: 'Dentist at general Dental HealthCare Hospital',
                ifollow: false,
            },
            {
                username: 'gmichael',
                avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSFNubinejiQCzktzhOyaoLc_BpB7CqoErwsMyzNAWxFOa7srz2',
                description : 'Phd in Physics by MIT',
                ifollow: false,
        }]);
    },
    follow(username) {
        return mockasync({})
    },
    unfollow(username) {
        return mockasync({})
    },
    get_user_details(username) {
        return mockasync(users_details[username])
    },
    list_questions(username) {
        if(!username) {
            var usersQuestionsList = []
            for (var allusername in users_questions) {
                usersQuestionsList.push({question: users_questions[allusername], details: users_details[allusername]})
            }
            return mockasync(usersQuestionsList);
        }
        return mockasync([{question: users_questions[username], details: users_details[username]}]);
    },
    get_question(question_title, author_username) {
        if (question_title == 'What is E=mc²?' && author_username == 'alberteinstein') {
            return mockasync({question: users_questions[author_username], details: users_details[author_username]});
        }
        if (question_title == 'Why? Why? Tell them that\'s human nature. Is it true?' && author_username == 'mjackson') {
            return mockasync({question: users_questions[author_username], details: users_details[author_username]});
        }
        if (question_title == 'Where are all the good songs nowadays?' && author_username == 'gmichael') {
            return mockasync({question: users_questions[author_username], details: users_details[author_username]});
        }
        return mockasync({});
    },
    get_answers(question_title, author_username) {
        if (question_title == 'What is E=mc²?' && author_username == 'alberteinstein') {
            return mockasync(
                [
                    {
                        answer: {
                            id: '1',
                            author_name: 'Michael Jackson',
                            author_username: 'mjackson',
                            text: "E = mc², equation in German-born physicist Albert Einstein’s theory of special relativity that expresses the fact that mass and energy are the same physical entity and can be changed into each other. In the equation, the increased relativistic mass (m) of a body times the speed of light squared (c2) is equal to the kinetic energy (E) of that body."
                        },
                        details: users_details['mjackson'], 
                    },
                    {
                        answer: {
                            id: '2',
                            author_name: 'George Michael',
                            author_username: 'gmichael',
                            text: "In physics, mass–energy equivalence states that anything having mass has an equivalent amount of energy and vice versa, with these fundamental quantities directly relating to one another by Albert Einstein's famous formula E=mc². This formula states that the equivalent energy (E) can be calculated as the mass (m) multiplied by the speed of light (c = ~3×108 m/s) squared. Similarly, anything having energy exhibits a corresponding mass m given by its energy E divided by the speed of light squared c2. Because the speed of light is a very large number in everyday units, the formula implies that even an everyday object at rest with a modest amount of mass has a very large amount of energy intrinsically. Chemical reactions, nuclear reactions, and other energy transformations may cause a system to lose some of its energy content (and thus some corresponding mass), releasing it as the radiant energy of light or as thermal energy for example."
                        },
                        details: users_details['gmichael'],                   }
                ],
            );
        } else if (question_title == 'Why? Why? Tell them that\'s human nature. Is it true?' && author_username == 'mjackson') {
            return mockasync([
                 {
                    answer: {
                        id: '3',
                        author_name: 'Albert Einstein',
                        author_username: 'alberteinstein',
                        text: "The Human nature has some ferocious feelings that can turn anyone into a beast. So, it' accurate to blema the human nature for some events."
                    },
                    details: users_details['alberteinstein'],
                }
            ]);
        }
        return mockasync([]);
    },
    post_question(text) {
        return mockasync({
            question: {
                author_name: logged_user.username,
                author_username: logged_user.username,
                created_at: '2019-10-03T15:52:48.943372',
                title: text,
            },
            details: {
                username: logged_user.username,
                avatar : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROUX4e_XOhgUT9wGMnGM27F6S7f-oBr7OgxeUCXV3DXTKAKIfc',
                description: 'Newbie on Quora',
                ifollow: false,
            }
        })
    },
    post_answer(question_title, author_username, text) {
        return mockasync({
             answer: {
                id: '4',
                author_name: logged_user.username,
                author_username: logged_user.username,
                text: text,
            },
            details: {
                username: logged_user.username,
                avatar : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROUX4e_XOhgUT9wGMnGM27F6S7f-oBr7OgxeUCXV3DXTKAKIfc',
                description: 'Newbie on Quora',
                ifollow: false,
            }
        })
    },
    post_new_user(user) {
        return mockasync({})
    },
    get_profile(username) {
        return mockasync({
            first_name: 'Mario',
            username: username,
            email:  'fake@fake.com',
            avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROUX4e_XOhgUT9wGMnGM27F6S7f-oBr7OgxeUCXV3DXTKAKIfc',
            description: "To be or not to be"
        })
    }
};

export default api;
