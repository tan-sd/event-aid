<script setup>
import { ref } from "vue";
import Scrollbar from "@/components/Scrollbar.vue";

const expandedIndex = ref(null);
const buttonText = ref(Array(10).fill("Sign up"));
const liked = ref(Array(10).fill(false));

function toggleDetails(index) {
    expandedIndex.value = expandedIndex.value === index ? null : index;
}

function handleButtonClick(index) {
    liked.value[index] = !liked.value[index];
    buttonText.value[index] = liked.value[index]
        ? "Sign up confirmed"
        : "Sign up";
}
</script>

<template>
    <main>
        <div class="welcome-container">
            <div class="profile-picture"></div>
            <div class="welcome-message">Hi, John Doe!</div>
            <div class="col-auto">
                <button
                    type="button"
                    data-bs-toggle="modal"
                    data-bs-target="#exampleModal"
                    class="btn btn-primary bg-orange"
                >
                    <font-awesome-icon icon="fa-solid fa-plus" /> Add Events
                </button>
                <RouterLink
                    to="/login"
                    class="btn btn-primary bg-orange"
                    style="margin-left: 10px"
                >
                    Log out
                </RouterLink>
            </div>
        </div>

        <div
            class="modal fade"
            id="exampleModal"
            tabindex="-1"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
        >
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                            Add New Event
                        </h5>
                        <button
                            type="button"
                            class="btn-close"
                            data-bs-dismiss="modal"
                            aria-label="Close"
                        ></button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="eventTitle" class="form-label"
                                    >Title</label
                                >
                                <input
                                    type="text"
                                    class="form-control"
                                    id="eventTitle"
                                />
                            </div>
                            <div class="mb-3">
                                <label for="eventDescription" class="form-label"
                                    >Description</label
                                >
                                <textarea
                                    class="form-control"
                                    id="eventDescription"
                                ></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="eventDate" class="form-label"
                                    >Date</label
                                >
                                <input
                                    type="date"
                                    class="form-control"
                                    id="eventDate"
                                />
                            </div>
                            <div class="mb-3">
                                <label for="eventTime" class="form-label"
                                    >Time</label
                                >
                                <input
                                    type="time"
                                    class="form-control"
                                    id="eventTime"
                                />
                            </div>
                            <div class="mb-3">
                                <label for="eventLocation" class="form-label"
                                    >Location</label
                                >
                                <input
                                    type="text"
                                    class="form-control"
                                    id="eventLocation"
                                />
                            </div>
                            <div class="mb-3">
                                <label for="eventImage" class="form-label"
                                    >Image</label
                                >
                                <input
                                    type="file"
                                    class="form-control"
                                    id="eventImage"
                                />
                            </div>
                            <div class="mb-3">
                                <label for="eventPeople" class="form-label"
                                    >No. of People Allowed</label
                                >
                                <input
                                    type="number"
                                    class="form-control"
                                    id="eventPeople"
                                />
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary">
                            Submit
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="event-container">
            <div class="event-container-title">Your Events</div>
            <Scrollbar>
                <div class="" v-for="(event, index) in events" :key="index">
                    <div
                        class="card event-card"
                        style="width: 20rem; margin-bottom: 20px"
                    >
                        <img
                            src="/event-aid-logo.png"
                            class="card-img-top"
                            alt="..."
                        />
                        <div class="card-body">
                            <h5 class="card-title">{{ event.title }}</h5>
                            <p class="card-text">5 Sep 2024</p>
                            <p class="d-inline-flex gap-1">
                                <button
                                    class="btn btn-color"
                                    type="button"
                                    data-bs-toggle="collapse"
                                    :data-bs-target="'#collapseExample' + n"
                                    aria-expanded="false"
                                    :aria-controls="'collapseExample' + n"
                                    @click="toggleDetails(n)"
                                >
                                    {{
                                        expandedIndex === n
                                            ? "x"
                                            : "Click for more details"
                                    }}
                                </button>
                            </p>
                            <div class="collapse" :id="'collapseExample' + n">
                                <div class="card card-body">
                                    <div
                                        class="event-description"
                                        style="margin-bottom: 10px"
                                    >
                                        Lorem ipsum dolor sit amet consectetur
                                        adipisicing elit. Atque necessitatibus
                                        ab minus facilis iure. Minima iste
                                        eligendi officia unde esse.
                                    </div>
                                    <div
                                        class="event-location"
                                        style="margin-bottom: 10px"
                                    >
                                        Bukit Batok Community Center
                                    </div>
                                    <div class="btn-event-container">
                                        <button
                                            class="btn event-indicate"
                                            style="background-color: red"
                                            @click="handleButtonClick(n - 1)"
                                        >
                                            Delete Event
                                        </button>
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
export default {
    name: "PlannerHome",
    data() {
        return {
            events: [
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 2",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
                {
                    location: "amk",
                    title: "this is a test 3",
                    description: "heheh",
                    planner_username: "planner2",
                    datetime: "2021-10-10 10:00:00",
                    num_participants: 10,
                },
            ],
        };
    },
    methods: {
        fetchEvents() {
            // Fetch events from the API
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
}

.event-container-eldery {
    font-size: 24px;
    font-weight: bold;
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
.bg-orange {
    background-color: #fb923c;
    border-color: #fb923c;
}
.bg-orange:hover {
    background-color: #be6923;
    border-color: #be6923;
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
