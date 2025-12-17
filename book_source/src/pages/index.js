import React from 'react';
import clsx from 'clsx'; // Keep clsx for potential class utilities
import Link from '@docusaurus/Link'; // Keep Link for navigation
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css'; // Keep for local styles

import Heading from '@theme/Heading'; // Keep for headings if needed
import { FaBoltLightning } from "react-icons/fa6";
import { FaRobot, FaBrain, FaCode, FaBookOpen, FaCogs, FaRocket, FaRegStar } from 'react-icons/fa'; // New import for icons

// --- Component Imports (will be added as tasks progress) ---
// import HeroSection from '../components/HeroSection';
// import AboutSection from '../components/AboutSection';
// import StatsSection from '../components/StatsSection';
// import ModulesSection from '../components/ModulesSection';
// import CtaSection from '../components/CtaSection';

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics`}
      description="The Future of Robotics. Learn ROS 2 & Isaac Sim.">
      <main>
        {/* Hero Section */}
        <section className={clsx(styles.heroSection, 'hero-section')}>
          <div className="container">
            {/* Main Heading */}
            <Heading as="h1" className={clsx(styles.mainHeading, 'main-heading', 'text--white')}>
              Smart Robotics <br />
              <span className="text--accent">Intelligence</span> &amp; <span className="text--accent">Technology</span>
            </Heading>

            {/* Intro Paragraph */}
            <p className={clsx(styles.introParagraph, 'intro-paragraph')}>
              Embark on an exciting journey into the world of Physical AI and Humanoid Robotics.
              <br />
              Discover cutting-edge concepts and hands-on applications with ROS 2 and NVIDIA Isaac Sim.</p>

            {/* Primary Button */}
            <div className={styles.buttons}>
              <Link className={clsx('button', 'button--primary-book')} to="/docs/intro">
                Start Learning
              </Link>
            </div>
          </div>
        </section>


        {/* About The Course Section */}






<section className="about-section">
  {/* Left Column */}
  <div className="about-left">
    <h2>ABOUT THIS COURSE</h2>
    <h1>From Smart Robotics Theory to <span>Real-World Applications</span></h1>
    <p>
      The Physical AI Course is your comprehensive guide to mastering generative AI and humanoid robotics. 
      Dive deep into physical AI foundations, explore cutting-edge simulations, and build real-world robotic applications.
    </p>
    <ol>
      <li>Deep Understanding of AI and robotics integration</li>
      <li>Hands-on projects with ROS 2 & Isaac Sim</li>
      <li>Industry-ready deployment strategies</li>
    </ol>
  </div>

  {/* Right Column: Feature Boxes */}
  <div className="about-right">
    <div className="feature-box">
      <FaBrain size={48} />
      <p>Master fundamental AI concepts and physical system integration.</p>
    </div>
    <div className="feature-box">
      <FaBoltLightning size={48} />
      <p>Build and deploy real robotic applications using advanced AI.</p>
    </div>
    <div className="feature-box">
      <FaRobot size={48} />
      <p>Learn production-ready deployment and scaling techniques.</p>
    </div>
  </div>
</section>
    

        {/* Modules & Features Section */}
        {/* <section className={clsx(styles.modulesSection, 'modules-section')}>
          <div className="container">
            <div className="row">
              {/* Module Box 1 
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaBookOpen size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>Comprehensive Modules</Heading>
                  <p className={styles.moduleDescription}>Structured learning paths from beginner to advanced.</p>
                </div>
              </div>
              {/* Module Box 2 
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaCogs size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>ROS 2 Integration</Heading>
                  <p className={styles.moduleDescription}>Deep dive into the Robot Operating System 2 framework.</p>
                </div>
              </div>
              {/* Module Box 3 
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaRobot size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>Humanoid Robotics</Heading>
                  <p className={styles.moduleDescription}>Learn to program and control complex bipedal robots.</p>
                </div>
              </div>
              {/* Module Box 4 
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaBrain size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>AI & Machine Learning</Heading>
                  <p className={styles.moduleDescription}>Integrate advanced AI techniques for intelligent behavior.</p>
                </div>
              </div>
              {/* Module Box 5 
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaCode size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>Practical Coding</Heading>
                  <p className={styles.moduleDescription}>Hands-on coding with leading robotics platforms.</p>
                </div>
              </div>
              {/* Module Box 6
              <div className="col col--4">
                <div className={clsx(styles.moduleBox, 'module-box')}>
                  <FaRocket size={48} className={styles.moduleIcon} />
                  <Heading as="h3" className={styles.moduleHeading}>Career Advancement</Heading>
                  <p className={styles.moduleDescription}>Build a portfolio for a career in robotics and AI.</p>
                </div>
              </div>
            </div>
          </div>
        </section> */}


        <section className={clsx(styles.modulesSection, 'modules-section')}>
  <div className="container">
    <div className="row">

      {[
        {
          icon: <FaBookOpen />,
          title: "Comprehensive Modules",
          desc: "Structured learning paths from beginner to advanced."
        },
        {
          icon: <FaCogs />,
          title: "ROS 2 Integration",
          desc: "Deep dive into the Robot Operating System 2 framework."
        },
        {
          icon: <FaRobot />,
          title: "Humanoid Robotics",
          desc: "Learn to program and control complex bipedal robots."
        },
        {
          icon: <FaBrain />,
          title: "AI & Machine Learning",
          desc: "Integrate advanced AI techniques for intelligent behavior."
        },
        {
          icon: <FaCode />,
          title: "Practical Coding",
          desc: "Hands-on coding with leading robotics platforms."
        },
        {
          icon: <FaRocket />,
          title: "Career Advancement",
          desc: "Build a portfolio for a career in robotics and AI."
        }
      ].map((item, i) => (
        <div key={i} className="col col--4">
          <div className={styles.moduleBox}>
            <div className={styles.iconWrapper}>
              {item.icon}
            </div>
            <h3 className={styles.moduleHeading}>{item.title}</h3>
            <p className={styles.moduleDescription}>{item.desc}</p>
          </div>
        </div>
      ))}

    </div>
  </div>
</section>


        {/* Final Call-To-Action Section */}
        <section className={clsx(styles.ctaSection, 'cta-section')}>
          <div className="container">
            <p className={styles.ctaText}>Ready to start your journey in Physical AI?</p>
            <div className={styles.buttons}>
              <Link className={clsx('button', 'button--primary-book')} to="/docs/intro">
                Start Reading
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}