// 📡 Conexión en tiempo real con el sistema de alertas
class RealTimeMonitor {
    constructor() {
        this.initialize();
    }

    async initialize() {
        this.updateDateTime();
        this.loadRealTimeData();
        setInterval(() => this.updateDateTime(), 1000);
        setInterval(() => this.loadRealTimeData(), 30000);
    }

    updateDateTime() {
        const now = new Date();
        document.getElementById('current-time').textContent = 
            now.toLocaleTimeString('es-ES');
    }

    async loadRealTimeData() {
        try {
            // Simular datos en tiempo real (en producción conectaría a APIs reales)
            const mockData = {
                alerts: 0,
                lastEarthquake: { magnitude: 2.5, location: 'Golfo de Cádiz' },
                tideLevel: 1.8,
                weather: { temp: 24, wind: 15 }
            };

            this.updateUI(mockData);
        } catch (error) {
            console.error('Error loading real-time data:', error);
        }
    }

    updateUI(data) {
        // Actualizar contadores
        document.getElementById('alerts-active').textContent = data.alerts;
        
        // Actualizar información de sismos
        const seismicCard = document.querySelector('[data-type="seismic"] p');
        seismicCard.textContent = `Último sismo: ${data.lastEarthquake.magnitude}M ${data.lastEarthquake.location}`;
        
        // Actualizar información meteorológica
        const weatherCard = document.querySelector('[data-type="weather"] p');
        weatherCard.textContent = `Viento: ${data.weather.wind}km/h • Marea: ${data.tideLevel}m`;
    }
}

// 🎯 Inicializar la aplicación
document.addEventListener('DOMContentLoaded', () => {
    const monitor = new RealTimeMonitor();
    
    // Efectos de animación
    this.animateElements();
});

// ✨ Animaciones
function animateElements() {
    // Animación de cards al hacer scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease-out';
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    // Observar todos los cards
    document.querySelectorAll('.alert-card, .science-card, .resource-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });
}

// 🎨 Efectos visuales
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// 📊 Datos de ejemplo para demostración
const demoData = {
    alerts: 0,
    seismicActivity: 'normal',
    weatherConditions: 'stable',
    tideLevel: 1.8,
    lastUpdate: new Date().toISOString()
};

console.log('🌊 Sistema de monitorizado inicializado');
console.log('📡 Conectando con servidores de alerta...');
console.log('✅ Página web operativa');
