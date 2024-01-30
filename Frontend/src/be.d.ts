export type BeForm = {
    firstName: string;
    lastName: string;
    email?: string;
    phone?: string;
    githubUrl?: string;
    preferences?: "Backend" | "Frontend" | "Fullstack" | "Design" | "Project Management";
    massage: string
    other?: any;
}

export type BeFormUnverified = {
    firstName: FormControl<string | null>;
    lastName: FormControl<string | null>;
    email?: FormControl<string | null>;
    phone?: FormControl<string | null>;
    githubUrl?: FormControl<string | null>;
    preferences?: FormControl<string | null>;
    massage: FormControl<string | null>;

    other?: FormControl<string | null>;
}