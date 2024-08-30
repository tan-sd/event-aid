<template>
    <main>
        <div class="welcome-container">
            <div class="profile-picture"></div>
            <div class="welcome-message">Hi, John Doe!</div>
        </div>
    </main>
</template>

<style scoped>
.welcome-container {
    color: black;
    align-items: center;
    display: flex;
    flex-direction: row;
}

.profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid black;
}

.welcome-message {
    margin-left: 10px;
}
</style>
