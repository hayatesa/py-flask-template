const FIND_USER_BY_USERNAME_URL = '/api/user/username';
const LIST_USERS_URL = '/api/user';

new Vue({
    el: '#user-app',
    data: {
        user: {username: ''},
        users: [],
        msg: ''
    },
    methods: {
        findByUsername,
        listUsers
    },
    created,
    mounted
});

function created() {
    this.listUsers();
}

function mounted() {

}

function findByUsername() {
    let _this = this;
    if (!_this.user.username.trim()) {
        _this.msg = '请输入用户名';
        return;
    }
    _this.msg = '';
    fetch(`${FIND_USER_BY_USERNAME_URL}/${_this.user.username}`)
        .then(resp => resp.json())
        .then(data => _this.users = data.data)

}

function listUsers() {
    let _this = this;
    fetch(LIST_USERS_URL)
        .then(resp => resp.json())
        .then(data => _this.users = data.data)
}