const VERSION = 'v1.3.2';
const SEARCH_USER_BY_USERNAME_URL = `/api/${VERSION}/sys/user/username`;
const SEARCH_USERS_URL = `/api/${VERSION}/sys/user/list`;

new Vue({
    el: '#user-app',
    data: {
        user: {username: ''},
        users: [],
        msg: ''
    },
    methods: {
        searchByUsername,
        searchUsers,
        enterToSearch,
        checkSearchInput,
    },
    created,
    mounted
});

function created() {
    this.searchUsers();
}

function mounted() {

}

function checkSearchInput() {
    if (!this.user.username.trim()) {
        this.msg = '请输入用户名';
        return false;
    }
    this.msg = '';
    return true;
}
function enterToSearch($event) {
    if ($event.keyCode === 13) {
        this.searchByUsername();
    }
}

function searchByUsername() {
    let _this = this;
    if (!this.checkSearchInput()) return;
    fetch(`${SEARCH_USER_BY_USERNAME_URL}/${_this.user.username}`)
        .then(resp => resp.json())
        .then(data => _this.users = [data.data])

}

function searchUsers() {
    fetch(SEARCH_USERS_URL)
        .then(resp => resp.json())
        .then(data => this.users = data.data)
}