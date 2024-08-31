<template>
    <div class="login-container">
        <div class="logo-container">
            <img class="logo" src="/event-aid-logo.png" />
        </div>
        <div class="form-floating mb-3">
            <input
                type="email"
                class="form-control"
                id="floatingInput"
                placeholder="name@example.com"
                v-model="username"
            />
            <label for="floatingInput">Email</label>
        </div>
        <div class="form-floating">
            <input
                type="password"
                class="form-control"
                id="floatingPassword"
                placeholder="Password"
                v-model="password"
            />
            <label for="floatingPassword">Password</label>
        </div>
        <!-- <button type="submit">Login</button> -->
        <button class="router-link" @click="login_now()">Log in</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
</template>


<script>
    export default {
        name: 'Login',
        data() {
            return {
                errorMessage: null,
                username: '',
                password: '',
            };
        },
        methods: {
            login() {
                this.errorMessage = 'Invalid email or password';
            },
            checkusertype(username) {
                // checks user type and id (user type is the string at the start, id is the number at the end)
                var user_type = '';
                var user_id = '';

                // for loop and stop when char is a number
                for (var i = 0; i < username.length; i++) {
                    if (isNaN(username.charAt(i))) {
                        user_type += username.charAt(i)
                    } else {
                        user_id += username.charAt(i)
                    }
                }

                return [user_type, user_id]
            },
            login_now() {
                // Check usertype and id
                var user_data = this.checkusertype(this.username)
                var user_type = user_data[0]
                var user_id = user_data[1]

                // If user is elderly
                if (user_type.charAt(0) == 'e') {
                    this.$router.push({ name: 'elderlyHome'})
                } else if (user_type.charAt(0) == 'g') {
                    this.$router.push({ name: 'guardianHome'})
                } else if (user_type.charAt(0) == 'p') {
                    this.$router.push({ name: 'plannerHome'})
                } else {
                    this.errorMessage = 'Invalid email or password';
                }
            }
        },
    };
</script>


<style scoped>
.login-container {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 300px;
    padding: 20px;
    border-radius: 4px;
    color: black;
}

.logo {
    height: 80px;
    width: 80px;
}

.logo-text {
    font-size: 40px;
    font-weight: bold;
    margin-left: 10px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    font-size: 13px;
    letter-spacing: 0.04em;
}

.logo-container {
    align-items: center;
    display: flex;
    flex-direction: row;
    margin-bottom: 20px;
    justify-content: center;
}

.router-link {
    margin-top: 15px;
    display: block;
    text-align: center;
    padding: 15px 10px 15px 10px;
    background-color: #fb923c;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    text-decoration: none;
}

.router-link:hover {
    background-color: #ff7300;
}

.error-message {
    color: red;
    margin-top: 10px;
    text-align: center;
}
</style>
