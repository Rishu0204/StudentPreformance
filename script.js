// Planet data with detailed information
const planetData = {
    mercury: {
        name: "Mercury",
        description: "Mercury is the smallest planet in our Solar System and the closest to the Sun. It has extreme temperature variations and no atmosphere to speak of.",
        stats: {
            "Distance from Sun": "57.9 million km",
            "Diameter": "4,879 km",
            "Mass": "3.3 × 10²³ kg",
            "Day Length": "58.6 Earth days",
            "Year Length": "88 Earth days",
            "Temperature": "-173°C to 427°C",
            "Moons": "0",
            "Gravity": "3.7 m/s²"
        },
        scientificData: {
            "Composition": "Mercury has a large metallic core that makes up about 75% of its radius. The core is likely made of iron and is partially molten.",
            "Atmosphere": "Mercury has virtually no atmosphere, with only trace amounts of oxygen, sodium, hydrogen, helium, and potassium.",
            "Surface Features": "The surface is heavily cratered, similar to Earth's Moon, with large impact basins and smooth plains."
        },
        texture: "radial-gradient(circle at 30% 30%, #8c7853, #5d4e37)",
        moons: []
    },
    venus: {
        name: "Venus",
        description: "Venus is the hottest planet in our Solar System due to its thick, toxic atmosphere. It's often called Earth's twin due to similar size and mass.",
        stats: {
            "Distance from Sun": "108.2 million km",
            "Diameter": "12,104 km",
            "Mass": "4.87 × 10²⁴ kg",
            "Day Length": "243 Earth days",
            "Year Length": "225 Earth days",
            "Temperature": "462°C",
            "Moons": "0",
            "Gravity": "8.87 m/s²"
        },
        scientificData: {
            "Atmosphere": "Venus has a thick atmosphere composed of 96% carbon dioxide and 3.5% nitrogen, creating a runaway greenhouse effect.",
            "Surface Pressure": "The atmospheric pressure is 90 times greater than Earth's, equivalent to being 1 km underwater.",
            "Volcanic Activity": "Venus has more volcanoes than any other planet, with over 1,600 major volcanoes identified."
        },
        texture: "radial-gradient(circle at 30% 30%, #ffc649, #ff8c42)",
        moons: []
    },
    earth: {
        name: "Earth",
        description: "Earth is the only known planet to harbor life. It has liquid water, a protective atmosphere, and the perfect distance from the Sun.",
        stats: {
            "Distance from Sun": "149.6 million km",
            "Diameter": "12,756 km",
            "Mass": "5.97 × 10²⁴ kg",
            "Day Length": "24 hours",
            "Year Length": "365.25 days",
            "Temperature": "-89°C to 58°C",
            "Moons": "1",
            "Gravity": "9.8 m/s²"
        },
        scientificData: {
            "Atmosphere": "Earth's atmosphere is 78% nitrogen, 21% oxygen, and 1% other gases, providing the perfect conditions for life.",
            "Hydrosphere": "About 71% of Earth's surface is covered by water, with oceans containing 97% of all water on the planet.",
            "Biodiversity": "Earth is home to an estimated 8.7 million species, from microscopic bacteria to massive blue whales."
        },
        texture: "radial-gradient(circle at 30% 30%, #6b93d6, #4682b4, #2e5984)",
        moons: [
            {
                name: "Moon",
                description: "Earth's Moon is the fifth largest moon in the Solar System and plays a crucial role in stabilizing Earth's axial tilt.",
                stats: {
                    "Distance from Earth": "384,400 km",
                    "Diameter": "3,474 km",
                    "Mass": "7.35 × 10²² kg",
                    "Orbital Period": "27.3 days",
                    "Temperature": "-233°C to 123°C"
                }
            }
        ]
    },
    mars: {
        name: "Mars",
        description: "Mars, the Red Planet, is our most explored neighbor. It has the largest volcano and canyon in the Solar System.",
        stats: {
            "Distance from Sun": "227.9 million km",
            "Diameter": "6,792 km",
            "Mass": "6.39 × 10²³ kg",
            "Day Length": "24.6 hours",
            "Year Length": "687 Earth days",
            "Temperature": "-87°C to -5°C",
            "Moons": "2",
            "Gravity": "3.71 m/s²"
        },
        scientificData: {
            "Atmosphere": "Mars has a thin atmosphere composed of 95% carbon dioxide, 3% nitrogen, and 1.6% argon.",
            "Water Evidence": "Evidence suggests Mars once had liquid water on its surface, with dried riverbeds and lake beds still visible.",
            "Olympus Mons": "The largest volcano in the Solar System, standing 21 km high and 600 km wide."
        },
        texture: "radial-gradient(circle at 30% 30%, #cd5c5c, #a0522d)",
        moons: [
            {
                name: "Phobos",
                description: "The larger and closer of Mars' two moons, Phobos orbits Mars three times per day.",
                stats: {
                    "Distance from Mars": "9,376 km",
                    "Diameter": "22.5 km",
                    "Orbital Period": "7.6 hours",
                    "Shape": "Irregular"
                }
            },
            {
                name: "Deimos",
                description: "The smaller and more distant moon of Mars, Deimos is one of the smallest moons in the Solar System.",
                stats: {
                    "Distance from Mars": "23,463 km",
                    "Diameter": "12.4 km",
                    "Orbital Period": "30.3 hours",
                    "Shape": "Irregular"
                }
            }
        ]
    },
    jupiter: {
        name: "Jupiter",
        description: "Jupiter is the largest planet in our Solar System, a gas giant with a Great Red Spot storm larger than Earth.",
        stats: {
            "Distance from Sun": "778.5 million km",
            "Diameter": "142,984 km",
            "Mass": "1.898 × 10²⁷ kg",
            "Day Length": "9.9 hours",
            "Year Length": "12 Earth years",
            "Temperature": "-108°C",
            "Moons": "95+",
            "Gravity": "23.1 m/s²"
        },
        scientificData: {
            "Composition": "Jupiter is mostly hydrogen and helium, similar to the Sun's composition.",
            "Great Red Spot": "A giant storm that has been raging for at least 400 years and is larger than Earth.",
            "Magnetic Field": "Jupiter has the strongest magnetic field of any planet, 14 times stronger than Earth's."
        },
        texture: "radial-gradient(circle at 30% 30%, #d2691e, #b8860b, #8b4513)",
        moons: [
            {
                name: "Io",
                description: "The most volcanically active body in the Solar System, with over 400 active volcanoes.",
                stats: {
                    "Distance from Jupiter": "421,700 km",
                    "Diameter": "3,643 km",
                    "Orbital Period": "1.8 days",
                    "Notable Feature": "Sulfur volcanoes"
                }
            },
            {
                name: "Europa",
                description: "Europa likely has a subsurface ocean beneath its icy crust, making it a prime target in the search for life.",
                stats: {
                    "Distance from Jupiter": "671,034 km",
                    "Diameter": "3,122 km",
                    "Orbital Period": "3.5 days",
                    "Notable Feature": "Subsurface ocean"
                }
            },
            {
                name: "Ganymede",
                description: "The largest moon in the Solar System, larger than Mercury and with its own magnetic field.",
                stats: {
                    "Distance from Jupiter": "1,070,412 km",
                    "Diameter": "5,268 km",
                    "Orbital Period": "7.2 days",
                    "Notable Feature": "Own magnetic field"
                }
            }
        ]
    },
    saturn: {
        name: "Saturn",
        description: "Saturn is famous for its spectacular ring system. It's a gas giant that could float in water due to its low density.",
        stats: {
            "Distance from Sun": "1.43 billion km",
            "Diameter": "120,536 km",
            "Mass": "5.68 × 10²⁶ kg",
            "Day Length": "10.7 hours",
            "Year Length": "29 Earth years",
            "Temperature": "-139°C",
            "Moons": "146+",
            "Gravity": "9.0 m/s²"
        },
        scientificData: {
            "Ring System": "Saturn's rings are made of billions of ice and rock particles, ranging from tiny grains to house-sized chunks.",
            "Density": "Saturn is the least dense planet, with a density of 0.687 g/cm³ - less than water.",
            "Hexagonal Storm": "Saturn has a unique hexagonal storm at its north pole, each side longer than Earth's diameter."
        },
        texture: "radial-gradient(circle at 30% 30%, #fad5a5, #deb887)",
        moons: [
            {
                name: "Titan",
                description: "Saturn's largest moon has a thick atmosphere and liquid methane lakes on its surface.",
                stats: {
                    "Distance from Saturn": "1,221,830 km",
                    "Diameter": "5,150 km",
                    "Orbital Period": "16 days",
                    "Notable Feature": "Methane lakes"
                }
            },
            {
                name: "Enceladus",
                description: "This icy moon has geysers that shoot water ice into space from its south pole.",
                stats: {
                    "Distance from Saturn": "238,020 km",
                    "Diameter": "504 km",
                    "Orbital Period": "1.4 days",
                    "Notable Feature": "Ice geysers"
                }
            },
            {
                name: "Mimas",
                description: "Known for the large Herschel crater that gives it a Death Star-like appearance.",
                stats: {
                    "Distance from Saturn": "185,539 km",
                    "Diameter": "396 km",
                    "Orbital Period": "22.6 hours",
                    "Notable Feature": "Herschel crater"
                }
            }
        ]
    },
    uranus: {
        name: "Uranus",
        description: "Uranus is an ice giant that rotates on its side. It has a faint ring system and extreme seasons.",
        stats: {
            "Distance from Sun": "2.87 billion km",
            "Diameter": "51,118 km",
            "Mass": "8.68 × 10²⁵ kg",
            "Day Length": "17.2 hours",
            "Year Length": "84 Earth years",
            "Temperature": "-197°C",
            "Moons": "27+",
            "Gravity": "8.7 m/s²"
        },
        scientificData: {
            "Rotation": "Uranus rotates on its side with an axial tilt of 98°, possibly due to a collision with an Earth-sized object.",
            "Composition": "Made mostly of water, methane, and ammonia ices surrounding a small rocky core.",
            "Magnetic Field": "Uranus has an unusual magnetic field that doesn't align with its rotational axis."
        },
        texture: "radial-gradient(circle at 30% 30%, #4fd0e7, #4169e1)",
        moons: [
            {
                name: "Miranda",
                description: "A small moon with extreme geological features and varied terrain.",
                stats: {
                    "Distance from Uranus": "129,390 km",
                    "Diameter": "471 km",
                    "Orbital Period": "1.4 days",
                    "Notable Feature": "Extreme terrain"
                }
            },
            {
                name: "Ariel",
                description: "The brightest of Uranus's moons with a young, geologically active surface.",
                stats: {
                    "Distance from Uranus": "190,900 km",
                    "Diameter": "1,158 km",
                    "Orbital Period": "2.5 days",
                    "Notable Feature": "Young surface"
                }
            },
            {
                name: "Titania",
                description: "The largest moon of Uranus with canyons and impact craters.",
                stats: {
                    "Distance from Uranus": "436,300 km",
                    "Diameter": "1,578 km",
                    "Orbital Period": "8.7 days",
                    "Notable Feature": "Large canyons"
                }
            }
        ]
    },
    neptune: {
        name: "Neptune",
        description: "Neptune is the windiest planet with speeds up to 2,100 km/h. It's a deep blue ice giant in the outer Solar System.",
        stats: {
            "Distance from Sun": "4.5 billion km",
            "Diameter": "49,528 km",
            "Mass": "1.02 × 10²⁶ kg",
            "Day Length": "16.1 hours",
            "Year Length": "165 Earth years",
            "Temperature": "-201°C",
            "Moons": "16+",
            "Gravity": "11.0 m/s²"
        },
        scientificData: {
            "Winds": "Neptune has the fastest winds in the Solar System, reaching speeds of up to 2,100 km/h.",
            "Great Dark Spot": "A storm system similar to Jupiter's Great Red Spot, though it has since disappeared.",
            "Discovery": "Neptune was the first planet discovered through mathematical prediction rather than observation."
        },
        texture: "radial-gradient(circle at 30% 30%, #4169e1, #191970)",
        moons: [
            {
                name: "Triton",
                description: "Neptune's largest moon orbits backwards and has nitrogen geysers.",
                stats: {
                    "Distance from Neptune": "354,759 km",
                    "Diameter": "2,707 km",
                    "Orbital Period": "5.9 days",
                    "Notable Feature": "Retrograde orbit"
                }
            },
            {
                name: "Nereid",
                description: "A small, irregularly shaped moon with a highly eccentric orbit.",
                stats: {
                    "Distance from Neptune": "5,513,818 km",
                    "Diameter": "340 km",
                    "Orbital Period": "360 days",
                    "Notable Feature": "Eccentric orbit"
                }
            }
        ]
    }
};

// Application state
let currentState = 'initial'; // 'initial', 'solar-system', 'planet-detail', 'moon-detail'
let selectedPlanet = null;
let selectedMoon = null;

// DOM elements
const initialScreen = document.getElementById('initial-screen');
const mainView = document.getElementById('main-view');
const sun = document.getElementById('sun');
const solarSystem = document.getElementById('solar-system');
const planetDetail = document.getElementById('planet-detail');
const moonDetail = document.getElementById('moon-detail');
const planetNavButtons = document.querySelectorAll('.planet-nav-btn');
const planets = document.querySelectorAll('.planet');

// Initialize the application
function init() {
    setupEventListeners();
    setupPlanetTextures();
}

// Setup all event listeners
function setupEventListeners() {
    // Sun click to transition to main view
    sun.addEventListener('click', transitionToMainView);
    
    // Planet navigation buttons
    planetNavButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const planetName = e.target.dataset.planet;
            selectPlanet(planetName);
        });
    });
    
    // Planet clicks in solar system view
    planets.forEach(planet => {
        planet.addEventListener('click', (e) => {
            e.stopPropagation();
            const planetName = e.currentTarget.dataset.planet;
            selectPlanet(planetName);
        });
    });
    
    // Click outside functionality
    document.addEventListener('click', handleClickOutside);
    
    // Prevent clicks inside detail views from bubbling
    planetDetail.addEventListener('click', (e) => e.stopPropagation());
    moonDetail.addEventListener('click', (e) => e.stopPropagation());
}

// Setup planet textures based on data
function setupPlanetTextures() {
    Object.keys(planetData).forEach(planetName => {
        const planet = document.querySelector(`.planet.${planetName} .planet-sphere`);
        if (planet) {
            planet.style.background = planetData[planetName].texture;
        }
    });
}

// Transition from initial screen to main solar system view
function transitionToMainView() {
    currentState = 'solar-system';
    
    initialScreen.classList.add('fade-out');
    
    setTimeout(() => {
        initialScreen.style.display = 'none';
        mainView.classList.remove('hidden');
        mainView.classList.add('fade-in');
    }, 1000);
}

// Select and display planet details
function selectPlanet(planetName) {
    if (currentState === 'moon-detail') {
        // If we're in moon detail, transition back to planet detail first
        transitionFromMoonToPlanet();
        setTimeout(() => selectPlanet(planetName), 500);
        return;
    }
    
    selectedPlanet = planetName;
    currentState = 'planet-detail';
    
    // Update active navigation button
    planetNavButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.planet === planetName);
    });
    
    // Get planet data
    const data = planetData[planetName];
    
    // Populate planet detail view
    populatePlanetDetail(data);
    
    // Show planet detail view with transition
    planetDetail.classList.add('active', 'fade-in');
    solarSystem.classList.add('detail-mode');
    
    // Setup moon event listeners for this planet
    setupMoonListeners(data.moons);
}

// Populate planet detail view with data
function populatePlanetDetail(data) {
    const planetName = document.getElementById('planet-name');
    const planetStats = document.getElementById('planet-stats');
    const planetDescription = document.getElementById('planet-description');
    const scientificData = document.getElementById('scientific-data');
    const selectedPlanetElement = document.getElementById('selected-planet');
    const planetMoons = document.getElementById('planet-moons');
    
    // Set planet name
    planetName.textContent = data.name;
    
    // Set planet texture
    selectedPlanetElement.style.background = data.texture;
    
    // Add special effects for specific planets
    if (data.name === 'Earth') {
        selectedPlanetElement.style.backgroundImage = `
            radial-gradient(circle at 20% 50%, #228b22 15px, transparent 15px),
            radial-gradient(circle at 60% 30%, #228b22 10px, transparent 10px),
            radial-gradient(circle at 80% 70%, #228b22 12px, transparent 12px)
        `;
    } else if (data.name === 'Jupiter') {
        selectedPlanetElement.style.backgroundImage = `repeating-linear-gradient(
            90deg,
            transparent,
            transparent 15px,
            rgba(139, 69, 19, 0.3) 15px,
            rgba(139, 69, 19, 0.3) 25px
        )`;
    }
    
    // Populate stats
    planetStats.innerHTML = '';
    Object.entries(data.stats).forEach(([label, value]) => {
        const statItem = document.createElement('div');
        statItem.className = 'stat-item';
        statItem.innerHTML = `
            <div class="stat-label">${label}</div>
            <div class="stat-value">${value}</div>
        `;
        planetStats.appendChild(statItem);
    });
    
    // Set description
    planetDescription.innerHTML = `<p>${data.description}</p>`;
    
    // Set scientific data
    scientificData.innerHTML = '<h3>Scientific Research & Discoveries</h3>';
    Object.entries(data.scientificData).forEach(([title, content]) => {
        const section = document.createElement('div');
        section.innerHTML = `<h4>${title}</h4><p>${content}</p>`;
        scientificData.appendChild(section);
    });
    
    // Setup moons display
    planetMoons.innerHTML = '';
    if (data.moons.length > 0) {
        data.moons.forEach((moon, index) => {
            const moonElement = document.createElement('div');
            moonElement.className = `planet-moon moon-${index + 1}`;
            moonElement.style.cssText = `
                position: absolute;
                width: 20px;
                height: 20px;
                background: radial-gradient(circle at 30% 30%, #c0c0c0, #808080);
                border-radius: 50%;
                cursor: pointer;
                transition: all 0.3s ease;
            `;
            
            // Position moons around the planet
            const angle = (index * 120) * (Math.PI / 180);
            const radius = 180;
            const x = Math.cos(angle) * radius;
            const y = Math.sin(angle) * radius;
            
            moonElement.style.transform = `translate(${x}px, ${y}px)`;
            moonElement.dataset.moonIndex = index;
            
            planetMoons.appendChild(moonElement);
        });
    }
}

// Setup moon event listeners
function setupMoonListeners(moons) {
    const moonElements = document.querySelectorAll('.planet-moon');
    moonElements.forEach(moonEl => {
        moonEl.addEventListener('click', (e) => {
            e.stopPropagation();
            const moonIndex = parseInt(e.target.dataset.moonIndex);
            selectMoon(moons[moonIndex]);
        });
    });
}

// Select and display moon details
function selectMoon(moonData) {
    selectedMoon = moonData;
    currentState = 'moon-detail';
    
    // Populate moon detail view
    populateMoonDetail(moonData);
    
    // Show moon detail view
    moonDetail.classList.add('active', 'fade-in');
    planetDetail.classList.remove('active');
}

// Populate moon detail view with data
function populateMoonDetail(moonData) {
    const moonName = document.getElementById('moon-name');
    const moonStats = document.getElementById('moon-stats');
    const moonDescription = document.getElementById('moon-description');
    
    moonName.textContent = moonData.name;
    moonDescription.innerHTML = `<p>${moonData.description}</p>`;
    
    // Populate moon stats
    moonStats.innerHTML = '';
    Object.entries(moonData.stats).forEach(([label, value]) => {
        const statItem = document.createElement('div');
        statItem.className = 'stat-item';
        statItem.innerHTML = `
            <div class="stat-label">${label}</div>
            <div class="stat-value">${value}</div>
        `;
        moonStats.appendChild(statItem);
    });
}

// Handle click outside functionality
function handleClickOutside(e) {
    if (currentState === 'moon-detail') {
        transitionFromMoonToPlanet();
    } else if (currentState === 'planet-detail') {
        transitionFromPlanetToSolarSystem();
    }
}

// Transition from moon detail back to planet detail
function transitionFromMoonToPlanet() {
    currentState = 'planet-detail';
    moonDetail.classList.remove('active', 'fade-in');
    planetDetail.classList.add('active');
    selectedMoon = null;
}

// Transition from planet detail back to solar system
function transitionFromPlanetToSolarSystem() {
    currentState = 'solar-system';
    planetDetail.classList.remove('active', 'fade-in');
    solarSystem.classList.remove('detail-mode');
    
    // Remove active state from navigation buttons
    planetNavButtons.forEach(btn => btn.classList.remove('active'));
    
    selectedPlanet = null;
}

// Smooth scrolling to planet (simulated by highlighting the selected planet)
function scrollToPlanet(planetName) {
    const planet = document.querySelector(`.planet.${planetName}`);
    if (planet) {
        // Add a temporary highlight effect
        planet.style.transform += ' scale(1.2)';
        planet.style.boxShadow = '0 0 30px rgba(255, 255, 255, 0.8)';
        
        setTimeout(() => {
            planet.style.transform = planet.style.transform.replace(' scale(1.2)', '');
            planet.style.boxShadow = '';
        }, 1000);
    }
}

// Add smooth hover effects for better UX
function addHoverEffects() {
    planets.forEach(planet => {
        planet.addEventListener('mouseenter', () => {
            if (currentState === 'solar-system') {
                planet.style.transform += ' scale(1.1)';
            }
        });
        
        planet.addEventListener('mouseleave', () => {
            if (currentState === 'solar-system') {
                planet.style.transform = planet.style.transform.replace(' scale(1.1)', '');
            }
        });
    });
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    init();
    addHoverEffects();
});

// Add keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        handleClickOutside();
    }
});