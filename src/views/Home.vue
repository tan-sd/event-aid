<template>
    <main>
        <div class="welcome-container">
            <div class="profile-picture"></div>
            <div class="welcome-message">Hi, John Doe!</div>
        </div>

        <div class="event-container">
            <div class="">Upcoming Events</div>
            <div class="" v-for="n in 10">
                <div class="card" style="width: 18rem">
                    <img src="..." class="card-img-top" alt="..." />
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">
                            Some quick example text to build on the card title
                            and make up the bulk of the card's content.
                        </p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
.welcome-container {
    margin: 40px 0 0 40px;
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

.event-container {
    margin: 40px 0 0 40px;
    color: black;
    align-items: center;
    /* display: flex; */
    /* flex-direction: row; */
}
</style>
