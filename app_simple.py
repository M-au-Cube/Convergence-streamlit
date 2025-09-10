import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Convergence",
    page_icon="🌐",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        padding: 2rem;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .header-content {
        flex: 1;
        text-align: left;
    }
    
    .logo-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin-left: 2rem;
    }
    
    .logo {
        max-width: 200px;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .section {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# En-tête principal avec logo à droite
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <div class="header-content">
        <h1 style="margin: 0; font-size: 2.5rem;">Convergence</h1>
        <p style="font-size: 1.2rem; margin: 0.5rem 0 0 0;">Votre partenaire pour un avenir durable et résilient</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Afficher le logo à droite
    try:
        st.image("Logo_Convergence.png", width=250)
    except:
        st.warning("⚠️ Logo non trouvé - vérifiez le chemin vers Logo_Convergence.png")

# Ajouter un séparateur visuel
st.markdown("---")

# Navigation par onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Présentation", 
    "📖 Cohérence", 
    "📅 Résilience", 
    "📊 Evidence", 
    "📞 Nous contacter"
])

with tab1:
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
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem;">$30T</div>
            <div style="font-size: 1rem; opacity: 0.9;">Actifs ESG mondiaux</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem;">+25%</div>
            <div style="font-size: 1rem; opacity: 0.9;">Croissance annuelle ESG</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem;">85%</div>
            <div style="font-size: 1rem; opacity: 0.9;">Entreprises avec rapports ESG</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem;">€1.2T</div>
            <div style="font-size: 1rem; opacity: 0.9;">Investissements durables EU</div>
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
    
    <div class="section">
        <h3>🌱 Les Notations ESG</h3>
        <p>Les <strong>critères ESG (Environnementaux, Sociaux et de Gouvernance)</strong> sont devenus 
        un standard incontournable pour évaluer la durabilité et la responsabilité des entreprises.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Les trois piliers ESG en colonnes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 1rem; background-color: #e8f5e8; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #2e7d32; margin: 0 0 0.5rem 0;">🌍 Environnemental</h4>
            <p style="margin: 0; font-size: 0.9rem;">Impact écologique, gestion des ressources, 
            émissions carbone, biodiversité</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 1rem; background-color: #e3f2fd; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #1976d2; margin: 0 0 0.5rem 0;">👥 Social</h4>
            <p style="margin: 0; font-size: 0.9rem;">Conditions de travail, diversité, 
            relations communautaires, droits humains</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 1rem; background-color: #fff3e0; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #f57c00; margin: 0 0 0.5rem 0;">⚖️ Gouvernance</h4>
            <p style="margin: 0; font-size: 0.9rem;">Transparence, éthique, 
            structure de management, conformité</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section">
        <p><strong>Pourquoi les notations ESG sont-elles importantes ?</strong></p>
        <ul>
            <li><strong>Pour les investisseurs :</strong> Évaluation des risques et opportunités à long terme</li>
            <li><strong>Pour les consommateurs :</strong> Choix éclairés basés sur les valeurs et l'impact</li>
            <li><strong>Pour les entreprises :</strong> Amélioration continue et différenciation concurrentielle</li>
            <li><strong>Pour la société :</strong> Transition vers un modèle économique plus durable</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="section">
        <h2>📖 Cohérence</h2>
        <p><strong>Cohérence</strong> est une base de données regroupant des données sur les entreprises, 
        leurs produits et les instruments financiers (actions, obligations, financements) qu'elles émettent.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section">
            <h3>Nos Offres</h3>
            <ul>
                <li><strong>Webscraping réputationnel :</strong> Collecte et analyse de données de réputation en ligne</li>
                <li><strong>Accès bases de données ESG :</strong> Accès privilégié aux données environnementales, sociales et de gouvernance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section">
            <h3>Informations Tarifaires</h3>
            <div style="background-color: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;">
                <p><strong>💰 Prix :</strong> Nous consulter</p>
                <p>Contactez-nous pour obtenir un devis personnalisé selon vos besoins spécifiques.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="section">
        <h2>📅 Résilience</h2>
        <p><strong>Résilience</strong> propose des questionnaires d'évaluation ESG et RSE des entreprises 
        et une aide pour réaliser et écrire les rapports de durabilité des entreprises.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section">
            <h3>Nos Services</h3>
            <ul>
                <li><strong>Questionnaires d'évaluation ESG :</strong> Outils d'évaluation des critères environnementaux, sociaux et de gouvernance</li>
                <li><strong>Questionnaires d'évaluation RSE :</strong> Évaluation de la responsabilité sociétale des entreprises</li>
                <li><strong>Aide à la rédaction :</strong> Accompagnement pour la réalisation et l'écriture des rapports de durabilité</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section">
            <h3>Informations Tarifaires</h3>
            <div style="background-color: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;">
                <p><strong>💰 Prix :</strong> Nous consulter</p>
                <p>Contactez-nous pour obtenir un devis personnalisé selon vos besoins spécifiques.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="section">
        <h2>📊 Evidence</h2>
        <p><strong>Evidence</strong> est une application qui permet aux utilisateurs de noter la durabilité 
        des produits qu'ils utilisent et de consulter la note ESG des produits qu'ils achètent.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section">
            <h3>Fonctionnalités</h3>
            <ul>
                <li><strong>Notation de durabilité :</strong> Évaluez la durabilité des produits que vous utilisez</li>
                <li><strong>Consultation des notes ESG :</strong> Consultez les notes environnementales, sociales et de gouvernance des produits</li>
                <li><strong>Base de données produits :</strong> Accès à une vaste base de données de produits évalués</li>
                <li><strong>Interface intuitive :</strong> Application facile à utiliser pour tous les consommateurs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section">
            <h3>Informations Tarifaires</h3>
            <div style="background-color: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;">
                <p><strong>💰 Prix :</strong> Nous consulter</p>
                <p>Contactez-nous pour obtenir un devis personnalisé selon vos besoins spécifiques.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("📱 L'application Evidence sera bientôt disponible sur les plateformes mobiles et web")

with tab5:
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
        <div style="background-color: #e3f2fd; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #2196f3;">
            <h3>Informations de Contact</h3>
            <p><strong>📧 Email :</strong> matt.mlb@icloud.com</p>
            <p><strong>📱 Téléphone :</strong> +33 6 62 86 11 39</p>
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

# Pied de page
st.markdown("""
<div style="text-align: center; padding: 2rem; background-color: #1e3c72; color: white; border-radius: 10px; margin-top: 2rem;">
    <p>&copy; 2025 Convergence. Tous droits réservés.</p>
    <p>Construit avec ❤️ et Streamlit</p>
</div>
""", unsafe_allow_html=True)
