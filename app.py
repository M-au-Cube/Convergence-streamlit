import streamlit as st
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Convergence",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour le style
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .logo {
        max-width: 200px;
        height: auto;
    }
    
    .tab-content {
        padding: 2rem;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    .section {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .section h3 {
        color: #1e3c72;
        border-bottom: 2px solid #2a5298;
        padding-bottom: 0.5rem;
    }
    
    .contact-info {
        background-color: #e3f2fd;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour charger le logo (sera mise à jour quand l'image sera fournie)
def load_logo():
    try:
        # Essayer de charger le logo depuis le dossier images
        logo_path = "images/logo.png"
        if Path(logo_path).exists():
            return logo_path
        logo_path = "images/logo.jpg"
        if Path(logo_path).exists():
            return logo_path
    except:
        pass
    return None

def main():
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>Convergence</h1>
        <p style="font-size: 1.2rem; margin: 0;">Votre partenaire pour un avenir durable et résilient</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation par onglets
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Présentation", 
        "🎯 Cohérence", 
        "🛡️ Résilience", 
        "📊 Evidence", 
        "📞 Nous contacter"
    ])
    
    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h2>Bienvenue chez Convergence</h2>
            <p>Convergence est une organisation dédiée à la transformation durable et à la résilience des systèmes. 
            Nous accompagnons les entreprises, les collectivités et les organisations dans leur transition vers 
            un modèle plus cohérent, résilient et basé sur des preuves concrètes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Métriques clés
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">50+</div>
                <div class="metric-label">Projets réalisés</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">25+</div>
                <div class="metric-label">Clients satisfaits</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">95%</div>
                <div class="metric-label">Taux de réussite</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">5</div>
                <div class="metric-label">Années d'expérience</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h3>Notre Mission</h3>
            <p>Accompagner la transformation des organisations vers des modèles plus durables, 
            cohérents et résilients, en s'appuyant sur des données et des preuves concrètes.</p>
        </div>
        
        <div class="section">
            <h3>Notre Vision</h3>
            <p>Un monde où chaque organisation contribue positivement à la société et à l'environnement, 
            tout en maintenant sa performance et sa résilience face aux défis futurs.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h2>🎯 Cohérence</h2>
            <p>La cohérence est au cœur de notre approche. Nous aidons les organisations à aligner 
            leurs stratégies, leurs actions et leurs valeurs pour créer une synergie durable.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="section">
                <h3>Notre Approche</h3>
                <ul>
                    <li><strong>Analyse systémique :</strong> Compréhension globale des enjeux</li>
                    <li><strong>Alignement stratégique :</strong> Cohérence entre vision et actions</li>
                    <li><strong>Intégration des parties prenantes :</strong> Engagement de tous les acteurs</li>
                    <li><strong>Mesure de l'impact :</strong> Suivi des résultats concrets</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="section">
                <h3>Services Proposés</h3>
                <ul>
                    <li>Audit de cohérence organisationnelle</li>
                    <li>Développement de stratégies intégrées</li>
                    <li>Formation et accompagnement des équipes</li>
                    <li>Mise en place d'indicateurs de performance</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h2>🛡️ Résilience</h2>
            <p>La résilience est la capacité d'une organisation à s'adapter, à se transformer 
            et à prospérer face aux changements et aux défis. Nous développons cette capacité 
            à travers une approche holistique et préventive.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h3>Piliers de la Résilience</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="section">
                <h4>🔧 Résilience Opérationnelle</h4>
                <p>Renforcement des processus, des systèmes et des capacités opérationnelles 
                pour faire face aux perturbations.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="section">
                <h4>👥 Résilience Organisationnelle</h4>
                <p>Développement des compétences, de la culture et de la structure 
                organisationnelle pour l'adaptation.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="section">
                <h4>🌍 Résilience Systémique</h4>
                <p>Intégration dans l'écosystème plus large et contribution à la 
                résilience collective.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h2>📊 Evidence</h2>
            <p>Nos interventions sont basées sur des preuves concrètes et des données fiables. 
            Nous mesurons, analysons et communiquons l'impact réel de nos actions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h3>Notre Méthodologie</h3>
            <p>Nous utilisons une approche rigoureuse basée sur :</p>
            <ul>
                <li><strong>Collecte de données :</strong> Métriques quantitatives et qualitatives</li>
                <li><strong>Analyse comparative :</strong> Benchmarking et études de cas</li>
                <li><strong>Validation scientifique :</strong> Méthodes éprouvées et reconnues</li>
                <li><strong>Communication transparente :</strong> Rapports détaillés et accessibles</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Graphique exemple (placeholder)
        st.markdown("""
        <div class="section">
            <h3>Impact Mesuré</h3>
            <p>Voici un exemple de nos résultats mesurés :</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Placeholder pour graphiques - sera remplacé par de vrais graphiques
        st.info("📈 Les graphiques d'impact seront intégrés ici avec les données réelles")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section">
            <h2>📞 Nous Contacter</h2>
            <p>Vous souhaitez en savoir plus sur nos services ou discuter de votre projet ? 
            N'hésitez pas à nous contacter.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="contact-info">
                <h3>Informations de Contact</h3>
                <p><strong>📧 Email :</strong> contact@convergence.fr</p>
                <p><strong>📱 Téléphone :</strong> +33 1 23 45 67 89</p>
                <p><strong>📍 Adresse :</strong> Paris, France</p>
                <p><strong>🌐 Site web :</strong> www.convergence.fr</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="section">
                <h3>Formulaire de Contact</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Formulaire de contact
            with st.form("contact_form"):
                nom = st.text_input("Nom *")
                email = st.text_input("Email *")
                entreprise = st.text_input("Entreprise")
                sujet = st.selectbox("Sujet", [
                    "Demande d'information",
                    "Devis",
                    "Partenariat",
                    "Autre"
                ])
                message = st.text_area("Message *", height=100)
                
                submitted = st.form_submit_button("Envoyer")
                
                if submitted:
                    if nom and email and message:
                        st.success("✅ Votre message a été envoyé avec succès !")
                    else:
                        st.error("❌ Veuillez remplir tous les champs obligatoires.")
        
        st.markdown("""
        <div class="section">
            <h3>Nos Horaires</h3>
            <p><strong>Lundi - Vendredi :</strong> 9h00 - 18h00</p>
            <p><strong>Samedi :</strong> 9h00 - 12h00</p>
            <p><strong>Dimanche :</strong> Fermé</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Pied de page
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background-color: #1e3c72; color: white; border-radius: 10px; margin-top: 2rem;">
        <p>&copy; 2024 Convergence. Tous droits réservés.</p>
        <p>Construit avec ❤️ et Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
