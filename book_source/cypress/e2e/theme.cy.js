describe('Theme E2E Tests', () => {
  beforeEach(() => {
    cy.visit('/docs/intro');
  });

  it('should apply the correct global theme styles', () => {
    cy.get('body').should('have.css', 'background-color', 'rgb(0, 0, 0)'); // Black
    cy.get('body').should('have.css', 'color', 'rgb(255, 255, 255)'); // White
    cy.get('html').should('have.css', 'font-family').and('match', /Poppins/);
  });

  it('should display the customized navbar', () => {
    cy.get('.navbar__title').should('be.visible').and('contain', '🤖 Physical AI & Humanoid Robotics');
    cy.get('.navbar__item.button--primary-book').contains('Get Started').should('be.visible');
  });

  it('should display the customized footer', () => {
    cy.get('.footer--dark').should('be.visible');
    cy.get('.footer--dark').should('contain', `Physical AI & Humanoid Robotics © ${new Date().getFullYear()} • The Future of Intelligent Machines`);
  });
});
