// Navigation functionality - Show only clicked section
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');
    
    // Function to show only the selected section
    function showSection(targetId) {
        sections.forEach(section => {
            if (section.id === targetId) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
        
        // Update active nav link
        navLinks.forEach(link => {
            if (link.getAttribute('href') === '#' + targetId) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }
    
    // Add click event to all nav links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            showSection(targetId);
        });
    });
    
    // Show profile section by default on page load
    showSection('profile');
});

// Prediction Form Functionality
document.addEventListener('DOMContentLoaded', function() {
    const predictionForm = document.getElementById('predictionForm');
    const predictBtn = document.getElementById('predictBtn');
    const predictionResult = document.getElementById('predictionResult');
    const predictionError = document.getElementById('predictionError');
    const resultContent = document.getElementById('resultContent');
    const resultDetails = document.getElementById('resultDetails');
    const errorMessage = document.getElementById('errorMessage');
    
    // Add focus effects to inputs
    const inputs = document.querySelectorAll('#predictionForm input, #predictionForm select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.borderColor = '#0071e3';
            this.style.boxShadow = '0 0 0 4px rgba(0, 113, 227, 0.1)';
        });
        
        input.addEventListener('blur', function() {
            this.style.borderColor = 'rgba(0, 0, 0, 0.1)';
            this.style.boxShadow = 'none';
        });
    });
    
    if (predictionForm) {
        predictionForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Get form values
            const formData = {
                temperature: parseFloat(document.getElementById('temperature').value),
                cloud_cover: parseFloat(document.getElementById('cloud_cover').value),
                humidity: parseFloat(document.getElementById('humidity').value),
                hour: parseInt(document.getElementById('hour').value),
                month: parseInt(document.getElementById('month').value)
            };
            
            // Hide previous results
            predictionResult.style.display = 'none';
            predictionError.style.display = 'none';
            
            // Update button state
            predictBtn.textContent = 'Predicting...';
            predictBtn.disabled = true;
            predictBtn.style.opacity = '0.6';
            
            try {
                // Make API request
                const response = await fetch('http://localhost:5000/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (response.ok && data.status === 'success') {
                    // Display prediction result
                    resultContent.textContent = `${data.predicted_solar_irradiance} W/m²`;
                    
                    // Add interpretation
                    let interpretation = '';
                    const irradiance = data.predicted_solar_irradiance;
                    
                    if (irradiance === 0) {
                        interpretation = 'No solar irradiance detected. This is typical for nighttime or very low light conditions.';
                    } else if (irradiance < 100) {
                        interpretation = 'Very low solar irradiance. Conditions are heavily overcast or it\'s early morning/late evening.';
                    } else if (irradiance < 300) {
                        interpretation = 'Low solar irradiance. Cloudy conditions are significantly reducing solar energy availability.';
                    } else if (irradiance < 600) {
                        interpretation = 'Moderate solar irradiance. Partly cloudy conditions with reasonable solar energy potential.';
                    } else if (irradiance < 800) {
                        interpretation = 'Good solar irradiance. Mostly clear sky with strong solar energy generation potential.';
                    } else {
                        interpretation = 'Excellent solar irradiance. Clear sky conditions with optimal solar energy generation.';
                    }
                    
                    resultDetails.textContent = interpretation;
                    predictionResult.style.display = 'block';
                } else {
                    // Display error
                    errorMessage.textContent = data.error || 'Prediction failed';
                    predictionError.style.display = 'block';
                }
            } catch (error) {
                // Display connection error
                errorMessage.textContent = 'Unable to connect to prediction service. Make sure the Flask API is running at http://localhost:5000';
                predictionError.style.display = 'block';
            } finally {
                // Reset button state
                predictBtn.textContent = 'Predict Solar Irradiance';
                predictBtn.disabled = false;
                predictBtn.style.opacity = '1';
            }
        });
        
        // Add hover effect to button
        predictBtn.addEventListener('mouseenter', function() {
            if (!this.disabled) {
                this.style.background = '#0077ED';
                this.style.transform = 'scale(1.01)';
            }
        });
        
        predictBtn.addEventListener('mouseleave', function() {
            this.style.background = '#0071e3';
            this.style.transform = 'scale(1)';
        });
    }
});
