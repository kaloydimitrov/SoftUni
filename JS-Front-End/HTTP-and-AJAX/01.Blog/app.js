function attachEvents() {
    const postsButton = document.getElementById("btnLoadPosts");
    const section = document.getElementById("posts");

    const viewButton = document.getElementById("btnViewPost");
    const postTitle = document.getElementById("post-title");
    const postBody = document.getElementById("post-body");
    const postComments = document.getElementById("post-comments");

    postsButton.addEventListener("click", () => {
        section.innerHTML = "";
        const postsURL = "http://localhost:3030/jsonstore/blog/posts";

        fetch(postsURL)
            .then((res) => res.json())
            .then((posts) => {
                for (const post in posts) {
                    const body = Object.values(posts[post])[0];
                    const id = Object.values(posts[post])[1];
                    const title = Object.values(posts[post])[2];

                    const newOption = document.createElement("option");
                    newOption.value = `${id}$${body}`;
                    newOption.textContent = title;

                    section.appendChild(newOption);
                }
            })
            .catch((err) => console.log(err))
    });

    viewButton.addEventListener("click", () => {
        postComments.innerHTML = "";
        const [sectionID, sectionBody] = section.value.split("$");
        const sectionTitle = section.options[section.selectedIndex].text;
        const commentsURL = "http://localhost:3030/jsonstore/blog/comments";

        postTitle.textContent = sectionTitle;
        postBody.textContent = sectionBody;

        fetch(commentsURL)
            .then((res) => res.json())
            .then((comments) => {
                for (const comment in comments) {
                    const id = Object.values(comments[comment])[0];
                    const postID = Object.values(comments[comment])[1];
                    const text = Object.values(comments[comment])[2];

                    if (postID == sectionID) {
                        const newLi = document.createElement("li");
                        newLi.textContent = text;
                        postComments.appendChild(newLi);
                    }
                }
            })
            .catch((err) => console.log(err))
    });
}

attachEvents();