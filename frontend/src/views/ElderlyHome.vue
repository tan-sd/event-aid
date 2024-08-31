<template>
    <main>
        <div class="welcome-container">
            <div class="profile-picture"></div>
            <div class="welcome-message">Hi, John Doe!</div>
            <div class="col-auto">
                <RouterLink
                    to="/login"
                    class="btn btn-primary bg-orange"
                    style="margin-left: 10px"
                >
                    Log out
                </RouterLink>
            </div>
        </div>

        <div class="event-container">
            <div class="event-container-title">Upcoming Events</div>
            <Scrollbar>
                <div v-for="e_event in all_events" :key="e_event.id">
                    <div class="card event-card" style="width: 20rem; margin-bottom: 20px">
                        <img src="https://picsum.photos/400/600" class="card-img-top"/>
                        
                        <div class="card-body">
                            <h5 class="card-title">{{ e_event.title }}</h5>
                            <p class="card-text">{{ e_event.datetime }}</p>
                            <p class="d-inline-flex gap-1">
                                <button
                                    class="btn btn-color"
                                    type="button"
                                    data-bs-toggle="collapse"
                                    :data-bs-target="'#collapseExample' + n"
                                    :aria-expanded="e_event.is_open"
                                    :aria-controls="'collapseExample' + n"
                                    @click="toggleOpen(e_event)"
                                >
                                    {{
                                        !e_event.is_open
                                            ? "Click for more details"
                                            : "x"
                                    }}
                                </button>
                            </p>

                            <div class="collapse" :id="'collapseExample' + n">
                                <div class="card card-body">
                                    <div
                                        class="event-description"
                                        style="margin-bottom: 10px"
                                    >
                                        {{ e_event.description }}
                                    </div>
                                    <div
                                        class="event-location"
                                        style="margin-bottom: 10px"
                                    >
                                        {{ e_event.location }}
                                    </div>
                                    <div class="btn-event-container">
                                        <button
                                            class="btn event-indicate"
                                            @click="handleButtonClick(e_event)"
                                        >
                                            {{ !e_event.is_signedup ? "I'm in!" : "I'm out!" }}
                                        </button>
                                        <div><font-awesome-icon icon="fa-solid fa-heart" /></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </Scrollbar>
        </div>
    </main>
</template>

<script>
import { ref } from "vue";
import Scrollbar from "@/components/Scrollbar.vue";

export default {
    name: "ElderlyHome",
    data() {
        return {
            elderly_name: "Bob",
            all_events: [
                {
                    "datetime": "Sun, 15 Sep 2024 10:00:00 GMT",
                    "description": "A health check-up for seniors.",
                    "id": 1,
                    "location": "Community Center",
                    "planner_username": "planner1",
                    "title": "Health Check-up",
                    "is_open": false,
                    "is_signedup": false,
                }, {
                    "datetime": "Fri, 20 Sep 2024 14:00:00 GMT",
                    "description": "A yoga session to promote wellness.",
                    "id": 2,
                    "location": "Park",
                    "planner_username": "planner2",
                    "title": "Yoga Session",
                    "is_open": false,
                    "is_signedup": false,
                }, {
                    "datetime": "Wed, 25 Sep 2024 09:00:00 GMT",
                    "description": "Reading session with a local author.",
                    "id": 3,
                    "location": "Library",
                    "planner_username": "planner1",
                    "title": "Book Reading",
                    "is_open": false,
                    "is_signedup": false,
                }
            ],
        };
    },
    methods: {
        toggleOpen(e_event) {
            e_event.is_open = !e_event.is_open;
        },
        handleButtonClick(e_event) {
            e_event.is_signedup = !e_event.is_signedup;
        },
    },
};
</script>

<style scoped>
.welcome-container {
    margin: 20px 0 0 30px;
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
    margin: 20px 0 0 30px;
    color: black;
    align-items: center;
    overflow: scroll;
}

.event-container-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.btn {
    background-color: #ff7300;
    color: #ffffff;
    font-size: 13px;
    letter-spacing: 0.04em;
}

.event-description,
.event-location {
    font-size: 13px;
    letter-spacing: 0.04em;
}

.btn-event-container {
    display: flex;
    flex-direction: row;
}

.event-heart-icon {
    background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/66955/web_heart_animation.png");
    background-repeat: no-repeat;
    background-size: 2900%;
    background-position: left;
    height: 50px;
    width: 50px;
    cursor: pointer;
}

.liked {
    background-position: right;
}

.animate {
    animation: heart-burst 0.8s steps(28) forwards;
}
@keyframes heart-burst {
    0% {
        background-position: left;
    }
    100% {
        background-position: right;
    }
}

.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: cover;
}

.col-auto {
    margin-left: auto;
    margin-right: 1rem;
}
</style>
