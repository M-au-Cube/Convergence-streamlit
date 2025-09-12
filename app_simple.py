import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

# Charger les variables d'environnement depuis .env (optionnel)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv n'est pas installé, on continue sans
except Exception:
    pass  # Erreur de lecture du fichier .env, on continue sans

# Import optionnel de SendGrid
try:
    import sendgrid
    from sendgrid.helpers.mail import Mail, Email, To, Content
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False
    st.warning("⚠️ Module SendGrid non installé. Utilisation du mode simulation pour les emails.")

# Configuration de la page
st.set_page_config(
    page_title="Convergence",
    page_icon="🌐",
    layout="wide"
)

# Fonction pour envoyer un email avec SendGrid
def send_email(nom, email, entreprise, sujet, message):
    try:
        # Vérification si SendGrid est disponible
        if not SENDGRID_AVAILABLE:
            return send_email_simulation(nom, email, entreprise, sujet, message)
        
        # Configuration SendGrid - Utilisation exclusive des secrets Streamlit
        try:
            SENDGRID_API_KEY = st.secrets["SENDGRID_API_KEY"]
            FROM_EMAIL = st.secrets["FROM_EMAIL"]
        except KeyError as e:
            st.error(f"❌ Secret manquant dans Streamlit: {e}")
            st.info("📝 Configurez vos secrets dans le fichier .streamlit/secrets.toml")
            return send_email_simulation(nom, email, entreprise, sujet, message)
        
        TO_EMAIL = "mattmoreau00@gmail.com"  # Test avec Gmail
        
        # Vérification du format de la clé API
        if not SENDGRID_API_KEY.startswith('SG.'):
            st.error("❌ Format de clé API SendGrid invalide. La clé doit commencer par 'SG.'")
            return send_email_simulation(nom, email, entreprise, sujet, message)
        
        # Création du message formaté
        email_body = f"""
Nouveau message de contact depuis le site Convergence

═══════════════════════════════════════════════════════════════

INFORMATIONS DU CONTACT :
• Nom : {nom}
• Email : {email}
• Entreprise : {entreprise if entreprise else 'Non renseignée'}
• Sujet : {sujet}

═══════════════════════════════════════════════════════════════

MESSAGE :
{message}

═══════════════════════════════════════════════════════════════

Message envoyé le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}
Depuis le site web Convergence (Streamlit App)

Pour répondre à ce contact, utilisez l'adresse : {email}
        """
        
        # Configuration SendGrid
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        
        # Création de l'email
        mail = Mail(
            from_email=Email(FROM_EMAIL, "Convergence Contact"),
            to_emails=To(TO_EMAIL),
            subject=f"Contact Convergence - {sujet}",
            plain_text_content=email_body
        )
        
        # Envoi de l'email
        response = sg.send(mail)
        
        if response.status_code == 202:
            st.success("✅ Message envoyé avec succès à matt.mlb@icloud.com !")
            st.balloons()
            return True
        elif response.status_code == 401:
            st.error("❌ Erreur d'authentification SendGrid (401 Unauthorized)")
            st.warning("🔑 Vérifiez votre clé API SendGrid dans les secrets Streamlit")
            st.info("📧 Assurez-vous que votre email expéditeur est vérifié dans SendGrid")
            return False
        elif response.status_code == 403:
            st.error("❌ Accès refusé SendGrid (403 Forbidden)")
            st.warning("🔑 Vérifiez les permissions de votre clé API")
            return False
        else:
            st.error(f"❌ Erreur SendGrid (Code: {response.status_code})")
            st.info("📋 Consultez la documentation SendGrid pour plus d'informations")
            return False
            
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "Unauthorized" in error_msg:
            st.error("❌ Erreur d'authentification SendGrid")
            st.warning("🔑 Vérifiez votre clé API SendGrid dans les secrets Streamlit")
        elif "403" in error_msg or "Forbidden" in error_msg:
            st.error("❌ Accès refusé SendGrid")
            st.warning("🔑 Vérifiez les permissions de votre clé API")
        else:
            st.error(f"❌ Erreur lors de l'envoi : {error_msg}")
        
        return send_email_simulation(nom, email, entreprise, sujet, message)

# Fonction de simulation (fallback)
def send_email_simulation(nom, email, entreprise, sujet, message):
    """Fonction de simulation pour le développement"""
    email_body = f"""
Nouveau message de contact depuis le site Convergence

INFORMATIONS DU CONTACT :
• Nom : {nom}
• Email : {email}
• Entreprise : {entreprise if entreprise else 'Non renseignée'}
• Sujet : {sujet}

MESSAGE :
{message}

Message envoyé le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}
Depuis le site web Convergence (Streamlit App)
    """
    
    st.success("✅ Message préparé pour envoi vers matt.mlb@icloud.com")
    st.info("📧 Mode simulation - Configurez SendGrid pour l'envoi réel")
    
    with st.expander("📋 Aperçu du message qui sera envoyé"):
        st.text(email_body)
    
    return True

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
        st.image("Logo_Convergence2.png", width=250)
    except:
        st.warning("⚠️ Logo non trouvé - vérifiez le chemin vers Logo_Convergence2.png")

# Ajouter un séparateur visuel
st.markdown("---")

# Navigation par onglets
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Présentation", 
    "📖 Cohérence", 
    "📅 Résilience", 
    "📊 Evidence", 
    "💻 Transparence",
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
    
    # Titre des métriques ESG
    st.markdown("""
    <div class="section">
        <h3>Quelques chiffres sur l'expansion des ESG :</h3>
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
        <h2>💻 Transparence</h2>
        <p><strong>Transparence</strong> est notre outil de dashboards ESG avancé qui offre aux entreprises 
        une visualisation complète et interactive de leurs données ESG, accompagnée d'un assistant IA 
        intelligent pour proposer des améliorations personnalisées.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section">
            <h3>📊 Dashboards ESG Interactifs</h3>
            <ul>
                <li><strong>Visualisation en temps réel :</strong> Tableaux de bord dynamiques avec métriques ESG actualisées</li>
                <li><strong>Analyses comparatives :</strong> Benchmarking sectoriel et historique</li>
                <li><strong>Indicateurs personnalisés :</strong> KPIs adaptés à votre secteur d'activité</li>
                <li><strong>Rapports automatisés :</strong> Génération de rapports ESG conformes aux standards</li>
                <li><strong>Alertes intelligentes :</strong> Notifications proactives sur les risques ESG</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section">
            <h3>🤖 Assistant IA pour l'Amélioration</h3>
            <ul>
                <li><strong>Analyse prédictive :</strong> Identification des tendances et risques futurs</li>
                <li><strong>Recommandations personnalisées :</strong> Actions concrètes pour améliorer votre score ESG</li>
                <li><strong>Optimisation des processus :</strong> Suggestions d'amélioration des pratiques internes</li>
                <li><strong>Conformité réglementaire :</strong> Veille automatique des nouvelles réglementations</li>
                <li><strong>Chat interactif :</strong> Interface conversationnelle pour vos questions ESG</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section">
        <h3>🎯 Fonctionnalités Clés</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Fonctionnalités en colonnes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 1rem; background-color: #e8f5e8; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #2e7d32; margin: 0 0 0.5rem 0;">📈 Analytics Avancés</h4>
            <p style="margin: 0; font-size: 0.9rem;">Machine Learning et IA pour l'analyse prédictive des données ESG</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 1rem; background-color: #e3f2fd; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #1976d2; margin: 0 0 0.5rem 0;">🔄 Intégration API</h4>
            <p style="margin: 0; font-size: 0.9rem;">Connexion directe avec vos systèmes existants et sources de données</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 1rem; background-color: #fff3e0; border-radius: 8px; text-align: center; margin-bottom: 1rem;">
            <h4 style="color: #f57c00; margin: 0 0 0.5rem 0;">📱 Interface Mobile</h4>
            <p style="margin: 0; font-size: 0.9rem;">Accès depuis n'importe où avec une interface responsive</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section">
        <h3>Informations Tarifaires</h3>
        <div style="background-color: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;">
            <p><strong>💰 Prix :</strong> Nous consulter</p>
            <p>Contactez-nous pour obtenir un devis personnalisé selon vos besoins spécifiques et la taille de votre organisation.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🚀 L'outil Transparence est actuellement en développement et sera bientôt disponible")

with tab6:
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
            <p><strong>📧 Votre message sera automatiquement envoyé à :</strong> matt.mlb@icloud.com</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du statut de configuration SendGrid
        if SENDGRID_AVAILABLE:
            try:
                api_key = st.secrets["SENDGRID_API_KEY"]
                from_email = st.secrets["FROM_EMAIL"]
                st.success("✅ SendGrid configuré - Envoi d'emails activé")
            except KeyError:
                st.warning("⚠️ SendGrid non configuré - Mode simulation activé")
                with st.expander("🔧 Comment configurer SendGrid"):
                    st.markdown("""
                    **Pour activer l'envoi d'emails réels :**
                    
                    1. **Créez un compte SendGrid** sur [sendgrid.com](https://sendgrid.com)
                    2. **Vérifiez un expéditeur** dans Settings → Sender Authentication
                    3. **Créez une clé API** dans Settings → API Keys
                    4. **Configurez les secrets** dans `.streamlit/secrets.toml` :
                       ```toml
                       SENDGRID_API_KEY = "SG.votre_cle_api"
                       FROM_EMAIL = "votre_email_verifie@votre-domaine.com"
                       ```
                    """)
        else:
            st.error("❌ Module SendGrid non installé")
            st.info("💡 Installez SendGrid avec : `pip install sendgrid`")
        
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
                    # Envoyer l'email
                    if send_email(nom, email, entreprise, sujet, message):
                        st.success("✅ Votre message a été envoyé avec succès à matt.mlb@icloud.com !")
                        st.balloons()
                    else:
                        st.error("❌ Une erreur est survenue lors de l'envoi du message.")
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
