<template>
    <div class="landing-container">
        <div class="logo-container">
            <img class="logo" src="/event-aid-logo.png" />
            <div class="logo-text">
                Event <span style="font-weight: normal">Aid</span>
            </div>
        </div>
        <div class="main-caption">Join the fun, stay connected.</div>
        <div class="sub-caption">
            Brings local events to your fingertips, making it easy for you to
            discover, join, and enjoy activities in your community!
        </div>
        <RouterLink class="router-link" to="/login">Join the fun</RouterLink>
    </div>
</template>

<style scoped>
.landing-container {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 400px;
    padding: 20px;
    border-radius: 4px;
    color: black;
}

.logo {
    height: 50px;
    width: 50px;
}

.logo-text {
    font-size: 30px;
    font-weight: bold;
    margin-left: 10px;
}

.form-group {
    margin-bottom: 15px;
}

input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 13px;
    letter-spacing: 0.04em;
    display: block;
    margin-bottom: 10px;
}

.logo-container {
    align-items: center;
    display: flex;
    flex-direction: row;
    margin-bottom: 10px;
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

.main-caption {
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
    line-height: 50px;
}

.sub-caption {
    font-size: 14px;
    margin-bottom: 20px;
}

.error-message {
    color: red;
    margin-top: 10px;
    text-align: center;
}
</style>
