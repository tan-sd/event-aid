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
            />
            <label for="floatingInput">Email</label>
        </div>
        <div class="form-floating">
            <input
                type="password"
                class="form-control"
                id="floatingPassword"
                placeholder="Password"
            />
            <label for="floatingPassword">Password</label>
        </div>
        <!-- <button type="submit">Login</button> -->
        <RouterLink class="router-link" to="/home">Log in</RouterLink>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
</template>

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
