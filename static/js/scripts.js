///*!
//* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
//* Copyright 2013-2023 Start Bootstrap
//* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
//*/
//// This file is intentionally blank
//// Use this file to add JavaScript to your project
//
//
document.addEventListener('DOMContentLoaded',()=>{
    const gallery = document.getElementById('gallery')

    loadPhotos();

    async function loadPhotos(){
    clearGallery();

    try{
    const response = await fetch('http://127.0.0.1:5000/api/');


    if(!response.ok){
    throw new Error(`HTTP error! status:${response.status}`);
    }

    const photos = await response.json();
    displayPhotos(photos);

    }catch(error){
    showError('failed to load photo')}
    }

    function displayPhotos(photos){
    photos.forEach(photo => {
    const photoCard = createPhotoCard(photo);
    gallery.appendChild(photoCard);
    });
    }

    function createPhotoCard(photo){
    const card = document.createElement('div');
    card.className='photo-card';

    const img = document.createElement('img');
    img.className='photo-img'
    img.src=photo.url;
    img.alt=photo.name;
    img.onerror = () =>{
    img.src = 'https://via.placeholder.com/300x200?text=Image+Not+Found';
    };

    const info = document.createElement('div')
    info.className='photo-info'

    const title = document.createElement('h3');
    title.className='photo-title';
    title.textContent= photo.name;

    const description = document.createElement('p');
    description.className='photo-description'
    description.textContent = photo.description;

    info.appendChild(title)
    info.appendChild(description)
    card.appendChild(img);
    card.appendChild(info);
//    card.appendChild(description);

    return card;
    }

    function clearGallery(){
    gallery.innerHTML='';}
})


    function sortPhotos(sortBy) {
        let sortedPhotos = [...originalPhotos];

        switch(sortBy) {
            case 'description-asc':
                sortedPhotos.sort((a, b) => a.description.localeCompare(b.description));
                break;
            case 'description-desc':
                sortedPhotos.sort((a, b) => b.description.localeCompare(a.description));
                break;
            case 'title-asc':
                sortedPhotos.sort((a, b) => a.title.localeCompare(b.title));
                break;
            case 'title-desc':
                sortedPhotos.sort((a, b) => b.title.localeCompare(a.title));
                break;
            case 'original':
            default:
                sortedPhotos = [...originalPhotos];
                break;
        }

//        // Update active button
//        updateActiveButton(sortBy);
//
//        // Store current sort
//        currentSort = sortBy;

        // Re-render gallery
        renderGallery(sortedPhotos);
    }

/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

//document.addEventListener('DOMContentLoaded', () => {
//    const gallery = document.getElementById('gallery');
//    let originalPhotos = []; // Store the original photos array
//    let currentSort = 'original'; // Track current sort method
//
//    // Load initial photos
//    loadPhotos();
//
//    // Sort event listener
//    const sortSelect = document.getElementById('sort-select');
//    if (sortSelect) {
//        sortSelect.addEventListener('change', (e) => {
//            sortPhotos(e.target.value);
//        });
//    }
//
//    async function loadPhotos() {
//        clearGallery();
//        showLoading(true);
//
//        try {
//            const response = await fetch('http://127.0.0.1:5000/api/');
//
//            if (!response.ok) {
//                throw new Error(`HTTP error! status: ${response.status}`);
//            }
//
//            const photos = await response.json();
//            originalPhotos = photos; // Store original photos
//            displayPhotos(photos);
//
//        } catch(error) {
//            showError('Failed to load photos');
//            console.error('Error loading photos:', error);
//        } finally {
//            showLoading(false);
//        }
//    }
//
//    function displayPhotos(photos) {
//        clearGallery();
//        photos.forEach(photo => {
//            const photoCard = createPhotoCard(photo);
//            gallery.appendChild(photoCard);
//        });
//    }
//
//    function createPhotoCard(photo) {
//        const card = document.createElement('div');
//        card.className = 'photo-card';
//
//        const img = document.createElement('img');
//        img.className = 'photo-img';
//        img.src = photo.url;
//        img.alt = photo.name || 'Photo';
//        img.onerror = () => {
//            img.src = 'https://via.placeholder.com/300x200?text=Image+Not+Found';
//        };
//
//        const info = document.createElement('div');
//        info.className = 'photo-info';
//
//        const title = document.createElement('h3');
//        title.className = 'photo-title';
//        title.textContent = photo.name || 'Untitled';
//
//        const description = document.createElement('p');
//        description.className = 'photo-description';
//        description.textContent = photo.description || 'No description available';
//
//        info.appendChild(title);
//        info.appendChild(description);
//        card.appendChild(img);
//        card.appendChild(info);
//
//        return card;
//    }
//
//    function sortPhotos(sortBy) {
//        if (originalPhotos.length === 0) return;
//
//        let sortedPhotos = [...originalPhotos];
//
//        switch(sortBy) {
//            case 'description-asc':
//                sortedPhotos.sort((a, b) => (a.description || '').localeCompare(b.description || ''));
//                break;
//            case 'description-desc':
//                sortedPhotos.sort((a, b) => (b.description || '').localeCompare(a.description || ''));
//                break;
//            case 'name-asc':
//                sortedPhotos.sort((a, b) => (a.name || '').localeCompare(b.name || ''));
//                break;
//            case 'name-desc':
//                sortedPhotos.sort((a, b) => (b.name || '').localeCompare(a.name || ''));
//                break;
//            case 'original':
//            default:
//                sortedPhotos = [...originalPhotos];
//                break;
//        }
//
//        currentSort = sortBy;
//        displayPhotos(sortedPhotos);
//    }
//
//    function clearGallery() {
//        gallery.innerHTML = '';
//    }
//
//    function showError(message) {
//        gallery.innerHTML = `
//            <div class="error-message">
//                <p>${message}</p>
//                <button onclick="loadPhotos()">Retry</button>
//            </div>
//        `;
//    }
//
//    function showLoading(show) {
//        const loading = document.getElementById('loading');
//        if (loading) {
//            loading.style.display = show ? 'block' : 'none';
//        }
//    }
//});