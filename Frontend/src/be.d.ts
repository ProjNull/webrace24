export type BeForm = {
    firstName: string;
    lastName: string;
    email?: string;
    phone?: string;
    githubUrl?: string;
    preferences?: "Backend" | "Frontend" | "Fullstack" | "Design" | "Project Management";

    other?: any;
}