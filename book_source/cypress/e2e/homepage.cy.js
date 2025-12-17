describe('Homepage E2E Tests', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should load the homepage and display the main hero content', () => {
    cy.get('.hero-center-box-text').should('be.visible').and('contain', 'The Future of Robotics');
    cy.get('.main-heading').should('be.visible').and('contain', 'Physical AI & Humanoid Robotics');
    cy.get('.button--primary-book').contains('Start Learning').should('be.visible');
  });

  it('should navigate to the introduction page when "Start Learning" button is clicked', () => {
    cy.get('.button--primary-book').contains('Start Learning').click();
    cy.url().should('include', '/docs/intro');
  });
});
