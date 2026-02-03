
import "../../public/styles/global-style.scss";


export const metadata = {
  title: "Project Presentation",
  description: "This is an app for presenting my data science projects",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
